import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from plot import load_tfevents as ltf


def main():
    # compare no baseline with nn baseline
    # logdirs = ["data\q2_pg_cheetah_HalfCheetah-v4_09-07-2025_22-49-44",
    #            "data\q2_pg_cheetah_baseline_HalfCheetah-v4_09-07-2025_22-54-40"]
    
    # compare different baseline gradient steps
    # logdirs = ["data\q2_pg_cheetah_baseline_HalfCheetah-v4_09-07-2025_22-54-40",
    #            "data\q2_pg_cheetah_baseline_bgs3_HalfCheetah-v4_09-07-2025_23-03-29",
    #            "data\q2_pg_cheetah_baseline_bgs1_HalfCheetah-v4_09-07-2025_23-06-42"]

    # compare with different baseline learning rate
    # logdirs = ["data\q2_pg_cheetah_baseline_HalfCheetah-v4_09-07-2025_22-54-40",
    #            "data\q2_pg_cheetah_baseline_blr0_005_HalfCheetah-v4_10-07-2025_13-53-46",
    #            "data\q2_pg_cheetah_baseline_blr0_001_HalfCheetah-v4_10-07-2025_14-00-56"]

    # compare with na
    logdirs = ["data\q2_pg_cheetah_baseline_HalfCheetah-v4_09-07-2025_22-54-40",
               "data\q2_pg_cheetah_baseline_na_HalfCheetah-v4_10-07-2025_15-28-04"]
    
    tags = ["Eval_AverageReturn", "Eval_StdReturn", "Train_EnvstepsSoFar","Baseline_Loss"]
    labels = ["-baseline -no na", "-baseline -na"]

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    for i,logdir in enumerate(logdirs):
        data = ltf.load_tfevents(logdir, tags)
        steps = data["Train_EnvstepsSoFar"]
        avg_return = data["Eval_AverageReturn"]
        std_return = data["Eval_StdReturn"]
        loss = data["Baseline_Loss"]

        plt.plot(steps, avg_return, linewidth=1.8, label=labels[i])
        plt.fill_between(steps, 
                    avg_return - std_return,
                    avg_return + std_return,
                    alpha=0.2,
                    label=None)
    
    plt.xlabel('Environment Steps', fontsize=12)
    plt.ylabel('Evaluation Average Return', fontsize=12)
    plt.title('HalfCheetah using neural network baseline with -na method', fontsize=14)
    plt.legend(loc='lower right')
    #plt.ylim(0,500)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()

