import numpy as np
from scipy import misc


def compute_mean_var(image, ground):
    num_pixels = 0
    mean = np.zeros(3)
    sum_val = np.zeros(3)

    assert image.shape[0] == ground.shape[0]
    assert image.shape[1] == ground.shape[1]

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if ground[i, j] > 0:
                sum_val += image[i, j]
                num_pixels += 1

    if num_pixels > 0:
        mean = sum_val / num_pixels

    var = np.zeros([3, 3])
    sum_val = np.zeros([3, 3])

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if ground[i, j] > 0:
                val = (image[i, j] - mean).reshape(-1, 1)
                sum_val += val.dot(val.T)

    if num_pixels > 0:
        var = sum_val / num_pixels

    return mean, var


def main():
    image_file = './images/flower.bmp'
    foreground_file = './images/foreground.bmp'
    background_file = './images/background.bmp'

    image = misc.imread(image_file, flatten= 0)
    foreground = misc.imread(foreground_file, flatten= 0)
    background = misc.imread(background_file, flatten= 0)

    mean_foreground, var_foreground = \
        compute_mean_var(image, foreground)

    mean_background, var_background = \
        compute_mean_var(image, background)

    print('Mean foreground', mean_foreground, 'Var foreground', var_foreground)
    print('Mean background', mean_background, 'Var background', var_background)


if __name__ == '__main__':
    main()
