import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from plot import load_tfevents as ltf


def main():

    logdirs = ["data\q2_pg_lunar_lander_lambda0_LunarLander-v2_09-07-2025_23-12-14",
               "data\q2_pg_lunar_lander_lambda95_LunarLander-v2_09-07-2025_23-23-22",
               "data\q2_pg_lunar_lander_lambda98_LunarLander-v2_09-07-2025_23-42-00",
               "data\q2_pg_lunar_lander_lambda99_LunarLander-v2_10-07-2025_08-29-18",
               "data\q2_pg_lunar_lander_lambda1_LunarLander-v2_10-07-2025_00-01-46"]
    
    tags = ["Eval_AverageReturn", "Eval_StdReturn", "Train_EnvstepsSoFar"]
    labels = ["lambda=0","lambda=0.95","lambda=0.98","lambda=0.99","lambda=1"]

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    for i,logdir in enumerate(logdirs):
        data = ltf.load_tfevents(logdir, tags)
        steps = data["Train_EnvstepsSoFar"]
        avg_return = data["Eval_AverageReturn"]
        std_return = data["Eval_StdReturn"]

        plt.plot(steps, avg_return, linewidth=1.5, label=labels[i])
        plt.fill_between(steps, 
                    avg_return - std_return,
                    avg_return + std_return,
                    alpha=0.2,
                    label=None)
    
    plt.xlabel('Environment Steps', fontsize=12)
    plt.ylabel('Evaluation Average Return', fontsize=12)
    plt.title('Lunaar Lander with different GAE lambda', fontsize=14)
    plt.legend(loc='lower right')

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()

