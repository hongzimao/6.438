import numpy as np


def ep(edge_potential, i, j, var_i, var_j):
    if (i, j) in edge_potential:
        return edge_potential[(i, j)][var_i, var_j]
    elif (j, i) in edge_potential:
        return edge_potential[(j, i)][var_j, var_i]
    else:
        return None


def get_msg(i, j, node_potential, edge_potential, messages, neighbors):
    # get msg_{i->j}(var)
    distant_msg = {0: 1, 1: 1}
    for k in neighbors[i]:
        if k != j:
            distant_msg[0] *= messages[(k, i)][0]
            distant_msg[1] *= messages[(k, i)][1]

    msg = {}
    msg[0] = node_potential[i][0] * ep(edge_potential, i, j, 0, 0) * distant_msg[0] \
           + node_potential[i][1] * ep(edge_potential, i, j, 1, 0) * distant_msg[1]
    msg[1] = node_potential[i][0] * ep(edge_potential, i, j, 0, 1) * distant_msg[0] \
           + node_potential[i][1] * ep(edge_potential, i, j, 1, 1) * distant_msg[1]

    return msg


def normalize_marginals(marginals):
    for node in marginals:
        p_sum = marginals[node][0] + marginals[node][1]
        marginals[node][0] /= p_sum
        marginals[node][1] /= p_sum


def belief_propagation(node_potential, edge_potential, diameter=np.inf):
    '''
    node_potential: {i -> node_potential}
    edge_potential: {(i, j) -> edge_potential}
    output: {i -> marginal}
    '''
    
    # find neighbor nodes for each node
    neighbors = {}
    for i in node_potential:
        neighbors[i] = set()
    for (i, j) in edge_potential:
        neighbors[i].add(j)
        neighbors[j].add(i)

    # initialize random message
    messages = {}
    init_msg = {0: 1, 1: 1}
    for (i, j) in edge_potential:
        messages[(i, j)] = init_msg
        messages[(j, i)] = init_msg

    d = min(diameter, len(node_potential))

    # tree diameter <= total number of nodes
    for _ in range(d):
        new_messages = {}
        for i in node_potential:
            for j in neighbors[i]:
                msg = get_msg(
                    i, j,
                    node_potential,
                    edge_potential,
                    messages,
                    neighbors)
                new_messages[(i, j)] = msg

        assert len(new_messages) == len(messages)
        messages = new_messages

    # compute marginals
    marginals = {}
    for i in node_potential:
        marginals[i] = {}
        msg = {0: 1, 1: 1}
        for j in neighbors[i]:
            msg[0] *= messages[(j, i)][0]
            msg[1] *= messages[(j, i)][1]
        marginals[i][0] = node_potential[i][0] * msg[0]
        marginals[i][1] = node_potential[i][1] * msg[1]

    # normalize marginals
    normalize_marginals(marginals)

    return marginals
