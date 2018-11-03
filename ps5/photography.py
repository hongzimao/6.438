import numpy as np
from scipy import misc
from bp import belief_propagation
from mean_var import compute_mean_var


def normalize_img(img):
    normalized_img = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                normalized_img[i, j, k] = float(img[i, j, k]) / 255.0
    return normalized_img


def visualize_marginals(img, marginals, file_name):
    array = np.zeros([img.shape[0], img.shape[1]])
    for (i, j) in marginals:
        array[i, j] = marginals[(i, j)][0]
    array = 1 - array  # revert black & white
    array *= 255
    misc.imsave(file_name, array)


def main():
    image_file = './images/flower.bmp'
    foreground_file = './images/foreground.bmp'
    background_file = './images/background.bmp'

    image = misc.imread(image_file, flatten= 0)
    image = normalize_img(image)  # between [0, 1]
    foreground = misc.imread(foreground_file, flatten= 0)
    background = misc.imread(background_file, flatten= 0)

    mean_foreground, var_foreground = \
        compute_mean_var(image, foreground)

    mean_background, var_background = \
        compute_mean_var(image, background)

    mean_foreground = mean_foreground.reshape(-1, 1)
    mean_background = mean_background.reshape(-1, 1)

    det_foreground = np.linalg.det(var_foreground)
    det_background = np.linalg.det(var_background)

    inv_foreground = np.linalg.inv(var_foreground)
    inv_background = np.linalg.inv(var_background)

    eps = 0.01

    # neighbor pixel edge potentials
    psi_neighbors = {}
    psi_neighbors[(0, 0)] = 0.9
    psi_neighbors[(1, 1)] = 0.9
    psi_neighbors[(0, 1)] = 0.1
    psi_neighbors[(1, 0)] = 0.1

    # fill in the potential functions
    node_potential = {}
    edge_potential = {}

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # node potential is influenced by the observation
            img_vec = image[i,j].reshape(-1, 1)
            node = {}
            node[1] = 1 / ((2 * np.pi) ** (3/2) * det_foreground ** (1/2)) * \
                np.exp(-0.5 * ((img_vec - mean_foreground).T.dot(inv_foreground)).dot(
                (img_vec - mean_foreground))) + eps
            node[0] = 1 / ((2 * np.pi) ** (3/2) * det_background ** (1/2)) * \
                np.exp(-0.5 * ((img_vec - mean_background).T.dot(inv_background)).dot(
                (img_vec - mean_background))) + eps
            node_potential[(i, j)] = node
            # edge potential among the pixels
            if i - 1 >= 0:
                if ((i - 1, j), (i, j)) not in edge_potential:
                    edge_potential[((i, j), (i - 1, j))] = psi_neighbors
            if i + 1 < image.shape[0]:
                if ((i + 1, j), (i, j)) not in edge_potential:
                    edge_potential[((i, j), (i + 1, j))] = psi_neighbors
            if j - 1 >= 0:
                if ((i, j - 1), (i, j)) not in edge_potential:
                    edge_potential[((i, j), (i, j - 1))] = psi_neighbors
            if j + 1 < image.shape[1]:
                if ((i, j + 1), (i, j)) not in edge_potential:
                    edge_potential[((i, j), (i, j + 1))] = psi_neighbors

    # get marginal at every step
    d = 0
    for marginals in belief_propagation(node_potential, edge_potential, 30):
        d += 1
        visualize_marginals(image, marginals,
            './images/marginals_iter_' + str(d) + '.png')
        print('Step', d)


if __name__ == '__main__':
    main()
