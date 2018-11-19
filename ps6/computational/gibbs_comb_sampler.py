import numpy as np
from collections import OrderedDict
from utils import OrderedSet, visualize, plot_mixing
from bp import belief_propagation


def sample(nodes, node_neighbors, edge_potential, traversal_order):
    '''
    nodes: list of (i, j) nodes
    nodes: dictionary node (i, j) -> neighbors of node (i, j)
    edge_potentials: dictionary ((i, j), (k, l)) -> potential map
    traversal_order: list of [(i, j)] for message passing
    '''
    node_potentials = {}
    tree_edge_potentials = {}

    last_node = set()
    for (i, j) in traversal_order:
        node_potentials[(i, j)] = {-1: 1, 1: 1}
        for n in node_neighbors[(i, j)]:
            # set up node potential based on observation on the other comb
            # those nodes shouldn't be on the traversal path
            if n not in traversal_order:
                node_potentials[(i, j)][-1] *= edge_potential[-1, nodes[n]]
                node_potentials[(i, j)][1] *= edge_potential[1, nodes[n]]
        # set up edge potential along the tree path
        assert len(last_node) <= 2
        for n in list(last_node):
            if n in node_neighbors[(i, j)]:
                tree_edge_potentials[(n, (i, j))] = edge_potential
                last_node.remove(n)
        last_node.add((i, j))

    # get message from one pass of belief propagation
    messages = belief_propagation(
        node_potentials, tree_edge_potentials, traversal_order)

    # reverse the traversal order, perform sampling
    samples = OrderedDict()  # need O(1) query and insertion order
    for (i, j) in reversed(traversal_order):
        ep_positive = 1
        ep_negative = 1
        for n in node_neighbors[(i, j)]:
            if n in traversal_order:
                if n in samples:
                    # already sampled
                    ep_positive *= edge_potential[1, samples[n]]
                    ep_negative *= edge_potential[-1, samples[n]]
                else:
                    # need to use message
                    ep_positive *= messages[(n, (i, j))][1]
                    ep_negative *= messages[(n, (i, j))][-1]

        # sample
        p = np.random.rand()

        if p < ep_positive / (ep_positive + ep_negative):
            samples[(i, j)] = 1
        else:
            samples[(i, j)] = -1

    return samples


def main():
    # parameters
    seed = 42
    size = 60
    theta = 0.45
    initial_value = 1
    iterations = 1001
    output_interval = 100
    results_folder = './results/'
    file_prefix = 'gibbs_comb_sampler'

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

    # find traversal order for block A
    traversal_order_a = OrderedSet()
    for j in range(size):
        if j % 2 == 0:
            for i in range(size - 2, -1, -1):
                traversal_order_a.add((i, j))
        else:
            traversal_order_a.add((0, j))

    # find traversal order for block B
    traversal_order_b = OrderedSet()
    for j in range(size):
        if j % 2 == 0:
            traversal_order_b.add((size - 1, j))
        else:
            for i in range(1, size, 1):
                traversal_order_b.add((i, j))

    # gibbs block sampling
    mean_vals = []
    for iteration in range(iterations):
        # sweep through bloack A and B
        for traversal_order in [traversal_order_a, traversal_order_b]:
            samples = sample(nodes, node_neighbors, edge_potential, traversal_order)
            for n in samples:
                nodes[n] = samples[n]

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
