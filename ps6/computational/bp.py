import numpy as np


def ep(edge_potential, i, j, var_i, var_j):
    if (i, j) in edge_potential:
        return edge_potential[(i, j)][var_i, var_j]
    elif (j, i) in edge_potential:
        return edge_potential[(j, i)][var_j, var_i]
    else:
        return None


def get_msg(i, j, node_potential, edge_potential, messages, neighbors, normalize=True):
    # get msg_{i->j}(var)
    distant_msg = {-1: 1, 1: 1}
    for k in neighbors[i]:
        if k != j:
            distant_msg[-1] *= messages[(k, i)][-1]
            distant_msg[1] *= messages[(k, i)][1]

    msg = {}
    msg[-1] = node_potential[i][-1] * ep(edge_potential, i, j, -1, -1) * distant_msg[-1] \
           + node_potential[i][1] * ep(edge_potential, i, j, 1, -1) * distant_msg[1]
    msg[1] = node_potential[i][-1] * ep(edge_potential, i, j, -1, 1) * distant_msg[-1] \
           + node_potential[i][1] * ep(edge_potential, i, j, 1, 1) * distant_msg[1]

    if normalize:
        s = msg[-1] + msg[1]
        msg[-1] /= s
        msg[1] /= s

    return msg


def belief_propagation(node_potential, edge_potential, traversal_order):
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
    init_msg = {-1: 1, 1: 1}
    for (i, j) in edge_potential:
        messages[(i, j)] = init_msg
        messages[(j, i)] = init_msg

    diam = min(diameter, len(node_potential))

    # traverse following the order
    for (i, j) in traversal_order:
        new_messages = {}
        msg = get_msg(
            i, j,
            node_potential,
            edge_potential,
            messages,
            neighbors)
        new_messages[(i, j)] = msg
        assert len(new_messages) == len(messages)
        messages = new_messages

    return messages
