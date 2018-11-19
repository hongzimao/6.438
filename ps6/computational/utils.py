import numpy as np
from scipy import misc


def visualize(size, nodes, file_name):
    array = np.zeros([size, size], dtype=np.uint8)
    # 1 is white, -1 is black
    for (i, j) in nodes:
        if nodes[i, j] == 1:
            array[i, j] = 255
        elif nodes[i, j] == -1:
            array[i, j] = 0
        else:
            print('Value has to be 1 or -1')
            exit(1)
    misc.imsave(file_name, array)
