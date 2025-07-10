import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from plot import load_tfevents as ltf


def main():
    # small batch
    # logdirs = ["data\q2_pg_cartpole_CartPole-v0_09-07-2025_21-46-34",
    #            "data\q2_pg_cartpole_rtg_CartPole-v0_09-07-2025_21-50-37",
    #            "data\q2_pg_cartpole_na_CartPole-v0_09-07-2025_21-51-42",
    #            "data\q2_pg_cartpole_rtg_na_CartPole-v0_09-07-2025_21-52-52"]
    
    # large batch
    logdirs = ["data\q2_pg_cartpole_lb_CartPole-v0_09-07-2025_22-25-13",
               "data\q2_pg_cartpole_lb_rtg_CartPole-v0_09-07-2025_22-28-30",
               "data\q2_pg_cartpole_lb_na_CartPole-v0_09-07-2025_22-31-41",
               "data\q2_pg_cartpole_lb_rtg_na_CartPole-v0_09-07-2025_22-34-57"]
    

    tags = ["Eval_AverageReturn", "Eval_StdReturn", "Train_EnvstepsSoFar"]
    labels = ["-vanilla","-rtg","-na","-rtg-na"]
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    for i,logdir in enumerate(logdirs):
        data = ltf.load_tfevents(logdir, tags)
        steps = data["Train_EnvstepsSoFar"]
        avg_return = data["Eval_AverageReturn"]
        std_return = data["Eval_StdReturn"]

        
        plt.plot(steps, avg_return, linewidth=1.8, label=labels[i])
        plt.fill_between(steps, 
                    avg_return - std_return,
                    avg_return + std_return,
                    alpha=0.2,
                    label=None)
    
    plt.xlabel('Environment Steps', fontsize=12)
    plt.ylabel('Evaluation Average Return', fontsize=12)
    plt.title('CartPole with large batch size 4000', fontsize=14)
    plt.legend(loc='lower right')

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

