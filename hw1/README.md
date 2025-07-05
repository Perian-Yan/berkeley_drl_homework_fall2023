## Setup

You can run this code on your own machine or on Google Colab. 

1. **Local option:** If you choose to run locally, you will need to install MuJoCo and some Python packages; see [installation.md](installation.md) for instructions.
2. **Colab:** The first few sections of the notebook will install all required dependencies. You can try out the Colab option by clicking the badge below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/berkeleydeeprlcourse/homework_fall2023/blob/master/hw1/cs285/scripts/run_hw1.ipynb)

## Complete the code

Fill in sections marked with `TODO`. In particular, edit
 - [policies/MLP_policy.py](cs285/policies/MLP_policy.py)
 - [infrastructure/utils.py](cs285/infrastructure/utils.py)
 - [scripts/run_hw1.py](cs285/scripts/run_hw1.py)

You have the option of running locally or on Colab using
 - [scripts/run_hw1.py](cs285/scripts/run_hw1.py) (if running locally) or [scripts/run_hw1.ipynb](cs285/scripts/run_hw1.ipynb) (if running on Colab)

See the homework pdf for more details.

## Run the code

Tip: While debugging, you probably want to keep the flag `--video_log_freq -1` which will disable video logging and speed up the experiment. However, feel free to remove it to save videos of your awesome policy!

If running on Colab, adjust the `#@params` in the `Args` class according to the commmand line arguments above.

### Section 1 (Behavior Cloning)
Command for problem 1:

```
python cs285/scripts/run_hw1.py 
	--expert_policy_file cs285/policies/experts/Ant.pkl 
	--env_name Ant-v4 --exp_name bc_ant --n_iter 1 
	--expert_data cs285/expert_data/expert_data_Ant-v4.pkl 
	--video_log_freq -1
```

For the evaluation, I use `eval_batch_size = 5000` and `ep_len = 1000`. This corresponds to approximately 5 rollouts.

```
python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/Ant.pkl --env_name Ant-v4 --exp_name bc_ant --n_iter 1 --expert_data cs285/expert_data/expert_data_Ant-v4.pkl --video_log_freq -1 --eval_batch_size 5000
```

Make sure to also try another environment.
See the homework PDF for more details on what else you need to run.
To generate videos of the policy, remove the `--video_log_freq -1` flag.

During the evaluation, two trajectories are sampled. The video below shows the learned policy (BC) for the four environments.
https://www.bilibili.com/video/BV1e439z9EhC/?spm_id_from=333.1387.homepage.video_card.click&vd_source=c15057271a519c1b36b7cc925e8cd5df

### Section 2 (DAgger)
Command for section 1:
(Note the `--do_dagger` flag, and the higher value for `n_iter`)

```
python cs285/scripts/run_hw1.py 
    --expert_policy_file cs285/policies/experts/Ant.pkl
    --env_name Ant-v4 --exp_name dagger_ant --n_iter 10 
    --do_dagger --expert_data cs285/expert_data/expert_data_Ant-v4.pkl 
	--video_log_freq -1
```

Make sure to also try another environment.
See the homework PDF for more details on what else you need to run.

I generate videos every 3 iterations (at `itr = 0, 3, 6, 9`):

```
python cs285/scripts/run_hw1.py --expert_policy_file cs285/policies/experts/Ant.pkl --env_name Ant-v4 --exp_name dagger_ant --n_iter 10 --do_dagger --expert_data cs285/expert_data/expert_data_Ant-v4.pkl --eval_batch_size 5000 --video_log_freq 3 
```

In step 0 (DAgger hasn't been used, same results as BC), the Walker2d cannot walk and easily fall. In step 3 (`itr = 3`), when DAgger is used, the Walker2d can already walk smoothly.

https://www.bilibili.com/video/BV1V439z9EXC/?spm_id_from=333.1387.homepage.video_card.click&vd_source=c15057271a519c1b36b7cc925e8cd5df

## Visualization the saved tensorboard event file:

You can visualize your runs using tensorboard:
```
tensorboard --logdir data
```

You will see scalar summaries as well as videos of your trained policies (in the 'images' tab).

You can choose to visualize specific runs with a comma-separated list:
```
tensorboard --logdir data/run1,data/run2,data/run3...
```

The above command doesn't work for me. For visualizing several tfevents, I put the folders, for example, `q2_dagger_ant_...` and `q2_dagger_halfcheetah_...` under a new folder `vidoe_dagger`,
and run
```
tensorboard --logdir video_data
```
Tensorboard will search and run all the tfevents under the folder `video_data`.

If running on Colab, you will be using the `%tensorboard` [line magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html) to do the same thing; see the [notebook](cs285/scripts/run_hw1.ipynb) for more details.

