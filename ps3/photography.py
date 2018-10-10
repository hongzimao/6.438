from bp import belief_propagation
from scipy import misc


phi_neutral = {}
phi_neutral[0] = 1
phi_neutral[1] = 1
phi = {0: {}, 1: {}}
phi[0][0] = 1
phi[0][1] = 0
phi[1][0] = 0
phi[1][1] = 1


def save_bmp(img, marginals, file_name):
    array = img.copy()
    for (i, j) in marginals:
        array[i, j] = marginals[(i, j)][0]

    array *= 255
    misc.imsave(file_name, array)


def image_denoise(img, alpha, beta):
    psi_alpha = {}
    psi_alpha[(0, 0)] = alpha
    psi_alpha[(1, 1)] = alpha
    psi_alpha[(0, 1)] = 1
    psi_alpha[(1, 0)] = 1
    psi_beta = {}
    psi_beta[(0, 0)] = 1 - beta
    psi_beta[(1, 1)] = 1 - beta
    psi_beta[(0, 1)] = beta
    psi_beta[(1, 0)] = beta

    node_potential = {}
    edge_potential = {}

    for i in range(1, img.shape[0] + 1):
        for j in range(1, img.shape[1] + 1):
            # node potential for actual value and observation
            node_potential[(i, j)] = phi_neutral
            node_potential[(-i, -j)] = phi[img[i - 1, j - 1]]
            # edge potential for noise
            edge_potential[((i, j), (-i, -j))] = psi_beta
            # edge potential among pixels
            if i - 1 > 0:
                if ((i - 1, j), (i, j)) not in edge_potential:
                    edge_potential[((i, j), (i - 1, j))] = psi_alpha
            if i + 1 <= img.shape[0]:
                if ((i + 1, j), (i, j)) not in edge_potential:
                    edge_potential[((i, j), (i + 1, j))] = psi_alpha
            if j - 1 > 0:
                if ((i, j - 1), (i, j)) not in edge_potential:
                    edge_potential[((i, j), (i, j - 1))] = psi_alpha
            if j + 1 <= img.shape[1]:
                if ((i, j + 1), (i, j)) not in edge_potential:
                    edge_potential[((i, j), (i, j + 1))] = psi_alpha

    marginals = belief_propagation(
        node_potential, edge_potential, diameter=img.shape[0] + img.shape[1])

    return marginals


def problem_ii():
    img = misc.imread('./black-white-small-noisy.bmp')
    img[img==255] = 1  # convert to binary
    beta = 0.1
    alphas = [2, 5, 10]
    for alpha in alphas:
        print('alpha', alpha, 'beta', beta)
        marginals = image_denoise(img, alpha, beta)
        save_bmp(img, marginals,
                 './ii_alpha_' + str(alpha) + \
                 '_beta_' + str(beta) + '.bmp')


def problem_iii():
    img = misc.imread('./black-white-small-noisy.bmp')
    img[img==255] = 1  # convert to binary
    alpha = 2
    betas = [0.05, 0.2, 0.4]
    for beta in betas:
        print('alpha', alpha, 'beta', beta)
        marginals = image_denoise(img, alpha, beta)
        save_bmp(img, marginals,
                 './iii_alpha_' + str(alpha) + \
                 '_beta_' + str(beta) + '.bmp')


if __name__ == '__main__':
    print('Problem (ii)')
    problem_ii()

    print('Problem (iii)')
    problem_iii()
