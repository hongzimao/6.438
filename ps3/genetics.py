from bp import belief_propagation


name_map = {'Orville': 1, 'Abraham': 2, 'Homer': 3, 'Lisa': 4,
            'Bart': 5, 'Maggie': 6, 'Hubert': 7, 'Tyrone': 8,
            'Frank': 9, 'Zeke': 10, 'Cryus': 11}


def round_marginals(marginals, r):
    rounded_marginals = {}
    for i in marginals:
        rounded_marginals[i] = {}
        for p in marginals[i]:
            rounded_marginals[i][p] = round(marginals[i][p], r)
    return rounded_marginals


def problem_i_before_conditioning():
    alphas = [2, 4, 6, 8, 10]
    for alpha in alphas:
        # edge potentials
        psi_ij = {}
        psi_ij[(0, 0)] = alpha
        psi_ij[(1, 1)] = alpha
        psi_ij[(0, 1)] = 1
        psi_ij[(1, 0)] = 1
        # node potentials
        phi_i = {}
        phi_i[0] = 1
        phi_i[1] = 1
        # set up node and edge potentials
        node_potential = {i: phi_i for i in range(1, 12)}
        edge_potential = {(i, j): psi_ij for (i, j) in
            [(1, 2), (2, 3), (3, 4), (3, 5), (3, 6),
            (1, 7), (7, 8), (8, 9), (8, 10), (7, 11)]}

        marginals = belief_propagation(node_potential, edge_potential)
        print('alpha', alpha, 'marginals', round_marginals(marginals, 4))


def problem_i_after_conditioning():
    alphas = [2, 4, 6, 8, 10]
    for alpha in alphas:
        # edge potentials
        psi_ij = {}
        psi_ij[(0, 0)] = alpha
        psi_ij[(1, 1)] = alpha
        psi_ij[(0, 1)] = 1
        psi_ij[(1, 0)] = 1
        # node potentials
        phi_neutral = {}
        phi_neutral[0] = 1
        phi_neutral[1] = 1
        phi_0 = {}
        phi_0[0] = 1
        phi_0[1] = 0
        phi_1 = {}
        phi_1[0] = 1
        phi_1[1] = 0
        # set up node and edge potentials
        node_potential = {i: phi_neutral for i in range(1, 12)}
        node_potential[4] = phi_1
        node_potential[5] = phi_0
        node_potential[6] = phi_0
        node_potential[9] = phi_1
        node_potential[10] = phi_1
        edge_potential = {(i, j): psi_ij for (i, j) in
            [(1, 2), (2, 3), (3, 4), (3, 5), (3, 6),
            (1, 7), (7, 8), (8, 9), (8, 10), (7, 11)]}

        marginals = belief_propagation(node_potential, edge_potential)
        print('alpha', alpha, 'marginals', round_marginals(marginals, 4))


if __name__ == '__main__':
    print('---- (i) after conditioning ----')
    problem_i_before_conditioning()
    print('---- (i) after conditioning ----')
    problem_i_after_conditioning()
