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
    seed = 42
    size = 60
    theta = 0.45
    initial_value = 1
    iterations = 1001
    output_interval = 100
    results_folder = './results/'
    file_prefix = 'gibbs_node_sampler'

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
