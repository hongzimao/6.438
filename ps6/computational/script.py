import os

os.system('python3 gibbs_node_sampler.py --initial_value 1 --file_prefix gibbs_node_sampler_positive')
os.system('python3 gibbs_node_sampler.py --initial_value -1 --file_prefix gibbs_node_sampler_negative')
os.system('python3 gibbs_comb_sampler.py --initial_value 1 --file_prefix gibbs_comb_sampler_positive')
os.system('python3 gibbs_comb_sampler.py --seed 4 --initial_value -1 --file_prefix gibbs_comb_sampler_negative')
os.system('python3 gibbs_node_sampler.py --initial_value 1 --iterations 50001 --output_interval 5000 --file_prefix gibbs_node_sampler_positive_long')
os.system('python3 gibbs_node_sampler.py --seed 4 --initial_value -1 --iterations 50001 --output_interval 5000 --file_prefix gibbs_node_sampler_negative_long')