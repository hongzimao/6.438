import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def main():
    node_positive = np.load('./results/gibbs_node_sampler_positive_long_mixing.npy')
    node_negative = np.load('./results/gibbs_node_sampler_negative_long_mixing.npy')
    node_random = np.load('./results/gibbs_node_sampler_random_long_mixing.npy')
    comb_positive = np.load('./results/gibbs_comb_sampler_positive_long_mixing.npy')
    comb_negative = np.load('./results/gibbs_comb_sampler_negative_long_mixing.npy')
    comb_random = np.load('./results/gibbs_comb_sampler_random_long_mixing.npy')

    font = {'family' : 'normal',
        'size'   : 14}
    matplotlib.rc('font', **font)

    fig = plt.figure(figsize=(6.35, 4))
    plt.plot(node_positive[:20000])
    plt.plot(node_negative[:20000])
    plt.plot(node_random[:20000])
    plt.xlabel('Step')
    plt.ylabel('Average value \n of all nodes')
    plt.title('Gibbs node-by-node sampler')
    # plt.legend(['Initialized at 1', 'Initialized at -1', 'Initialized randomly'], frameon=False, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.savefig('gibbs_node_sampler_mixing.pdf')
    plt.savefig('gibbs_node_sampler_mixing.png')
    plt.close(fig)

    fig = plt.figure(figsize=(9, 4))
    plt.plot(comb_positive[0:20000])
    plt.plot(comb_negative[0:20000])
    plt.plot(comb_random[0:20000])
    plt.xlabel('Step')
    plt.ylabel('Average value \n of all nodes')
    plt.title('Gibbs block sampler')
    plt.legend(['Initialized at 1', 'Initialized at -1', 'Initialized randomly'], frameon=False, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xticks([0, 5000, 10000, 15000, 20000])
    plt.tight_layout()
    plt.savefig('gibbs_block_sampler_mixing.pdf')
    plt.savefig('gibbs_block_sampler_mixing.png')
    plt.close(fig)

    # node_positive_theta_small = np.load('./results/gibbs_node_sampler_positive_theta_0.1_mixing.npy')
    # node_negative_theta_small = np.load('./results/gibbs_node_sampler_negative_theta_0.1_mixing.npy')

    # fig = plt.figure(figsize=(6, 4))
    # plt.plot(node_positive_theta_small)
    # plt.plot(node_negative_theta_small)
    # plt.xlabel('Step')
    # plt.ylabel('Average value \n of all nodes')
    # plt.title('Gibbs node-by-node sampler (theta = 0.1)')
    # plt.legend(['Initialized at 1', 'Initialized at -1'], frameon=False)
    # plt.tight_layout()
    # plt.savefig('gibbs_node_sampler_mixing_theta_0.1.pdf')
    # plt.close(fig)

    # node_positive_theta_small = np.load('./results/gibbs_node_sampler_positive_theta_0.2_mixing.npy')
    # node_negative_theta_small = np.load('./results/gibbs_node_sampler_negative_theta_0.2_mixing.npy')

    # fig = plt.figure(figsize=(6, 4))
    # plt.plot(node_positive_theta_small)
    # plt.plot(node_negative_theta_small)
    # plt.xlabel('Step')
    # plt.ylabel('Average value \n of all nodes')
    # plt.title('Gibbs node-by-node sampler (theta = 0.2)')
    # plt.legend(['Initialized at 1', 'Initialized at -1'], frameon=False)
    # plt.tight_layout()
    # plt.savefig('gibbs_node_sampler_mixing_theta_0.2.pdf')
    # plt.close(fig)

    # node_positive_theta_small = np.load('./results/gibbs_node_sampler_positive_theta_0.3_mixing.npy')
    # node_negative_theta_small = np.load('./results/gibbs_node_sampler_negative_theta_0.3_mixing.npy')

    # fig = plt.figure(figsize=(6, 4))
    # plt.plot(node_positive_theta_small)
    # plt.plot(node_negative_theta_small)
    # plt.xlabel('Step')
    # plt.ylabel('Average value \n of all nodes')
    # plt.title('Gibbs node-by-node sampler (theta = 0.3)')
    # plt.legend(['Initialized at 1', 'Initialized at -1'], frameon=False)
    # plt.tight_layout()
    # plt.savefig('gibbs_node_sampler_mixing_theta_0.3.pdf')
    # plt.close(fig)

    # node_positive_theta_small = np.load('./results/gibbs_node_sampler_positive_theta_0.4_mixing.npy')
    # node_negative_theta_small = np.load('./results/gibbs_node_sampler_negative_theta_0.4_mixing.npy')

    # fig = plt.figure(figsize=(6, 4))
    # plt.plot(node_positive_theta_small)
    # plt.plot(node_negative_theta_small)
    # plt.xlabel('Step')
    # plt.ylabel('Average value \n of all nodes')
    # plt.title('Gibbs node-by-node sampler (theta = 0.4)')
    # plt.legend(['Initialized at 1', 'Initialized at -1'], frameon=False)
    # plt.tight_layout()
    # plt.savefig('gibbs_node_sampler_mixing_theta_0.4.pdf')
    # plt.close(fig)



if __name__ == '__main__':
    main()