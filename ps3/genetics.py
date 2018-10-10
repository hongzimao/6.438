from bp import belief_propagation
from prettytable import PrettyTable


name_map = {'Orville': 1, 'Abraham': 2, 'Homer': 3, 'Lisa': 4,
            'Bart': 5, 'Maggie': 6, 'Hubert': 7, 'Tyrone': 8,
            'Frank': 9, 'Zeke': 10, 'Cryus': 11}
id_map = {name_map[k]: k for k in name_map}


def round_marginals(marginals, r):
    rounded_marginals = {}
    for i in marginals:
        rounded_marginals[i] = {}
        for p in marginals[i]:
            rounded_marginals[i][p] = round(marginals[i][p], r)
    return rounded_marginals

def print_marginals(marginals, r=4):
    rounded_marginals = round_marginals(marginals, r)
    t = PrettyTable(['Name', 'p(pollen allergy)', 'p(no pollen allergy)'])
    for i in id_map:
        t.add_row([id_map[i], rounded_marginals[i][1], rounded_marginals[i][0]])
    print(t)

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
        print('alpha', alpha)
        print_marginals(marginals)


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
        phi_1[0] = 0
        phi_1[1] = 1
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
        print('alpha', alpha)
        print_marginals(marginals)


def problem_ii():
    alphas = [2, 4, 6, 8, 10]
    betas = [0.8, 0.9]
    # 12, 13, 14, 15, 16 ->
    # Lisa, Bart, Maggie, Frank, Zeka's observations
    for alpha in alphas:
        for beta in betas:
            # edge potentials
            psi_alpha = {}
            psi_alpha[(0, 0)] = alpha
            psi_alpha[(1, 1)] = alpha
            psi_alpha[(0, 1)] = 1
            psi_alpha[(1, 0)] = 1
            psi_beta = {}
            psi_beta[(0, 0)] = beta
            psi_beta[(1, 1)] = beta
            psi_beta[(0, 1)] = 1 - beta
            psi_beta[(1, 0)] = 1 - beta
            # node potentials
            phi_neutral = {}
            phi_neutral[0] = 1
            phi_neutral[1] = 1
            phi_0 = {}
            phi_0[0] = 1
            phi_0[1] = 0
            phi_1 = {}
            phi_1[0] = 0
            phi_1[1] = 1
            # set up node and edge potentials
            node_potential = {i: phi_neutral for i in range(1, 17)}
            node_potential[12] = phi_1
            node_potential[13] = phi_0
            node_potential[14] = phi_0
            node_potential[15] = phi_1
            node_potential[16] = phi_1
            edge_potential = {(i, j): psi_alpha for (i, j) in
                [(1, 2), (2, 3), (3, 4), (3, 5), (3, 6),
                (1, 7), (7, 8), (8, 9), (8, 10), (7, 11)]}
            edge_potential[(4, 12)] = psi_beta
            edge_potential[(5, 13)] = psi_beta
            edge_potential[(6, 14)] = psi_beta
            edge_potential[(9, 15)] = psi_beta
            edge_potential[(10, 16)] = psi_beta

            marginals = belief_propagation(node_potential, edge_potential)
            print('alpha', alpha, 'beta', beta)
            print_marginals(marginals)


if __name__ == '__main__':
    print('================================')
    print('==== (i) before conditioning ====')
    print('================================')
    problem_i_before_conditioning()

    print('================================')
    print('==== (i) after conditioning ====')
    print('================================')
    problem_i_after_conditioning()

    print('================================')
    print('============= (ii) =============')
    print('================================')
    problem_ii()
