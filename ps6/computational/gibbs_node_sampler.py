import argparse
import numpy as np
from utils import visualize, plot_mixing


def sample(size, nodes, node_neighbors, edge_potential, node=None):
    '''
    nodes: list of (i, j) nodes
    nodes: dictionary node (i, j) -> neighbors of node (i, j)
    edge_potentials: dictionary ((i, j), (k, l)) -> potential map
    '''

    # sample a random node
    if node is None:
        i = np.random.randint(size)
        j = np.random.randint(size)
    else:
        i, j = node
    
    # probability for the node to be +1 / -1
    ep_positive = 1
    ep_negative = 1
    for n in node_neighbors[(i, j)]:
        ep_positive *= edge_potential[1, nodes[n]]
        ep_negative *= edge_potential[-1, nodes[n]]

    # sample a value
    p = np.random.rand()

    if p < ep_positive / (ep_positive + ep_negative):
        nodes[(i, j)] = 1
    else:
        nodes[(i, j)] = -1


def main():
    # parameters
    parser = argparse.ArgumentParser(description='parameters')
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--size', type=int, default=60)
    parser.add_argument('--theta', type=float, default=0.45)
    parser.add_argument('--initial_value', type=float, default=1)
    parser.add_argument('--iterations', type=int, default=1001)
    parser.add_argument('--output_interval', type=int, default=100)
    parser.add_argument('--results_folder', type=str, default='./results/')
    parser.add_argument('--file_prefix', type=str, default='gibbs_node_sampler')
    config = parser.parse_args()
    # assign parameters
    seed = config.seed
    size = config.size
    theta = config.theta
    initial_value = config.initial_value
    iterations = config.iterations
    output_interval = config.output_interval
    results_folder = config.results_folder
    file_prefix = config.file_prefix

    # random seed
    np.random.seed(seed)

    # initialize nodes
    nodes = {}
    for i in range(size):
        for j in range(size):
            if initial_value != 1 and initial_value != -1:
                nodes[(i, j)] = 2 * np.random.randint(2) - 1
            else:
                nodes[(i, j)] = initial_value

    # set up neighbor information
    node_neighbors = {}
    for i in range(size):
        for j in range(size):
            neighbors = []
            if i >= 1:
                neighbors.append((i - 1, j))
            if j >= 1:
                neighbors.append((i, j - 1))
            if i < size - 1:
                neighbors.append((i + 1, j))
            if j < size - 1:
                neighbors.append((i, j + 1))
            node_neighbors[(i, j)] = neighbors

    # set up edge potential
    edge_potential = {}
    edge_potential[(1, 1)] = np.exp(theta)
    edge_potential[(1, -1)] = np.exp(- theta)
    edge_potential[(-1, 1)] = np.exp(- theta)
    edge_potential[(-1, -1)] = np.exp(theta)


    # gibbs node-by-node sampling
    mean_vals = []
    mean_vals.append(np.mean(list(nodes.values())))
    for iteration in range(iterations):
        # sweep through all i and j
        for i in range(size):
            for j in range(size):
                sample(size, nodes, node_neighbors, edge_potential, (i, j))

        # record the mean values
        mean_vals.append(np.mean(list(nodes.values())))

        if iteration % output_interval == 0:
            # visualization
            visualize(size, nodes, results_folder + 
                file_prefix + '_iter_' + str(iteration) + '.png')
            print('iteration ', iteration)

    # plot mixing behavoir
    plot_mixing(mean_vals, results_folder + file_prefix + '_mixing')


if __name__ == '__main__':
    main()
