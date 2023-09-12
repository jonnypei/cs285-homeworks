### Section 1 (Behavior Cloning)

Problem (1):

To get the Ant statistics, run
```
python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/Ant.pkl --env_name Ant-v4 --exp_name bc_ant --n_iter 1 --expert_data cs285/expert_data/expert_data_Ant-v4.pkl --video_log_freq -1 --seed 4 --eval_batch_size 10000 --ep_len 1000
```

To get the Walker2d statistics, run
```
python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/Walker2d.pkl --env_name Walker2d-v4 --exp_name bc_walker2d --n_iter 1 --expert_data cs285/expert_data/expert_data_Walker2d-v4.pkl --video_log_freq -1 --seed 4 --eval_batch_size 10000 --ep_len 1000
```

Problem (2):

To get the numbers in the graph for Walker2d, run:
```
 python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/Walker2d.pkl --env_name Walker2d-v4 --exp_name bc_walker2d --n_iter 1 --expert_data cs285/expert_data/expert_data_Walker2d-v4.pkl --video_log_freq -1 --seed 4 --eval_batch_size 10000 --ep_len 1000 --n_layers [NUMBER OF HIDDEN LAYERS]
```
where you replace `[NUMBER OF HIDDEN LAYERS]` with 2, 3, ... 12.

### Section 2 (DAgger)

To get the numbers in the Ant graph, run:
```
 python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/Ant.pkl --env_name Ant-v4 --exp_name dagger_ant --n_iter 20 --do_dagger --expert_data cs285/expert_data/expert_data_Ant-v4.pkl --video_log_freq -1 --seed 4 --eval_batch_size 10000 --ep_len 1000
```

To get the numbers in the Walker2d graph, run:
```
 python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/Walker2d.pkl --env_name Walker2d-v4 --exp_name dagger_walker2d --n_iter 20 --do_dagger --expert_data cs285/expert_data/expert_data_Walker2d-v4.pkl --video_log_freq -1 --seed 4 --eval_batch_size 10000 --ep_len 1000
```