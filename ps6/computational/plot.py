import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def main():
    node_positive = np.load('./results/gibbs_node_sampler_positive_mixing.npy')
    node_negative = np.load('./results/gibbs_node_sampler_negative_mixing.npy')
    comb_positive = np.load('./results/gibbs_comb_sampler_positive_mixing.npy')
    comb_negative = np.load('./results/gibbs_comb_sampler_negative_mixing.npy')
    node_positive_long = np.load('./results/gibbs_node_sampler_positive_long_mixing.npy')
    node_negative_long = np.load('./results/gibbs_node_sampler_negative_long_mixing.npy')

    font = {'family' : 'normal',
        'size'   : 14}
    matplotlib.rc('font', **font)

    fig = plt.figure(figsize=(6, 4))
    plt.plot(node_positive)
    plt.plot(node_negative)
    plt.xlabel('Step')
    plt.ylabel('Average value \n of all nodes')
    plt.title('Gibbs node-by-node sampler')
    plt.legend(['Initialized at 1', 'Initialized at -1'], frameon=False)
    plt.tight_layout()
    plt.savefig('gibbs_node_sampler_mixing.pdf')
    plt.close(fig)

    fig = plt.figure(figsize=(6, 4))
    plt.plot(comb_positive)
    plt.plot(comb_negative)
    plt.xlabel('Step')
    plt.ylabel('Average value \n of all nodes')
    plt.title('Gibbs block sampler')
    plt.legend(['Initialized at 1', 'Initialized at -1'], frameon=False)
    plt.tight_layout()
    plt.savefig('gibbs_block_sampler_mixing.pdf')
    plt.close(fig)

    fig = plt.figure(figsize=(9, 4))
    plt.plot(node_positive_long)
    plt.plot(node_negative_long)
    plt.xlabel('Step')
    plt.ylabel('Average value \n of all nodes')
    plt.title('Gibbs node-by-node sampler (longer)')
    plt.legend(['Initialized at 1', 'Initialized at -1'], frameon=False, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.savefig('gibbs_node_sampler_mixing_longer.pdf')
    plt.close(fig)



if __name__ == '__main__':
    main()