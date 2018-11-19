import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from collections import OrderedDict


def plot_mixing(mean_vals, file_name):
    plt.plot(mean_vals)
    plt.xlabel('Step')
    plt.ylabel('Average value of all nodes')
    plt.tight_layout()
    plt.savefig(file_name + '.pdf')
    np.save(file_name + '.npy', mean_vals)


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


class OrderedSet(object):
    def __init__(self, contents=()):
        self.set = OrderedDict((c, None) for c in contents)

    def __contains__(self, item):
        return item in self.set

    def __iter__(self):
        return iter(self.set.keys())

    def __len__(self):
        return len(self.set)

    def __reversed__(self):
        return iter(reversed(self.set.keys()))

    def add(self, item):
        self.set[item] = None

    def clear(self):
        self.set.clear()

    def pop(self):
        item = next(iter(self.set))
        del self.set[item]
        return item

    def remove(self, item):
        del self.set[item]

    def to_list(self):
        return [k for k in self.set]