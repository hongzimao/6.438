import os

os.system('python3 gibbs_node_sampler.py --initial_value 1 --file_prefix gibbs_node_sampler_positive')
os.system('python3 gibbs_node_sampler.py --seed 4 --initial_value -1 --file_prefix gibbs_node_sampler_negative')
os.system('python3 gibbs_node_sampler.py --initial_value 1 --iterations 20001 --output_interval 2000 --file_prefix gibbs_node_sampler_positive_long')
os.system('python3 gibbs_node_sampler.py --seed 4 --initial_value -1 --iterations 20001 --output_interval 2000 --file_prefix gibbs_node_sampler_negative_long')
os.system('python3 gibbs_node_sampler.py --seed 123 --initial_value 0 --iterations 20001 --output_interval 2000 --file_prefix gibbs_node_sampler_random_long')
os.system('python3 gibbs_comb_sampler.py --iterations 20001 --output_interval 2000 --initial_value 1 --file_prefix gibbs_comb_sampler_positive_long')
os.system('python3 gibbs_comb_sampler.py --iterations 20001 --output_interval 2000 --seed 4 --initial_value -1 --file_prefix gibbs_comb_sampler_negative_long')
os.system('python3 gibbs_comb_sampler.py --iterations 20001 --output_interval 2000 --seed 123 --initial_value 0 --file_prefix gibbs_comb_sampler_random_long')

# for fun
os.system('python3 gibbs_node_sampler.py --initial_value 1 --theta 0.4 --file_prefix gibbs_node_sampler_positive_theta_0.4')
os.system('python3 gibbs_node_sampler.py --seed 4 --initial_value -1 --theta 0.4 --file_prefix gibbs_node_sampler_negative_theta_0.4')
os.system('python3 gibbs_node_sampler.py --initial_value 1 --theta 0.3 --file_prefix gibbs_node_sampler_positive_theta_0.3')
os.system('python3 gibbs_node_sampler.py --seed 4 --initial_value -1 --theta 0.3 --file_prefix gibbs_node_sampler_negative_theta_0.3')
os.system('python3 gibbs_node_sampler.py --initial_value 1 --theta 0.2 --file_prefix gibbs_node_sampler_positive_theta_0.3')
os.system('python3 gibbs_node_sampler.py --seed 4 --initial_value -1 --theta 0.2 --file_prefix gibbs_node_sampler_negative_theta_0.2')
os.system('python3 gibbs_node_sampler.py --initial_value 1 --theta 0.1 --file_prefix gibbs_node_sampler_positive_theta_0.1')
os.system('python3 gibbs_node_sampler.py --seed 4 --initial_value -1 --theta 0.1 --file_prefix gibbs_node_sampler_negative_theta_0.1')
