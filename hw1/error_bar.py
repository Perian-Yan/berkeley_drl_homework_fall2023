import numpy as np
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()

X = np.arange(10)
avg_return = [339.1794128417969,
2750.695313,
4642.51416015625,
5407.1689453125,
4469.052734,
5410.81494140625,
5233.2568359375,
5238.57470703125,
5301.72021484375,
5410.69775390625,
]

#train_loss = [0.073, 0.061, 0.056, 0.0495]

std = [306.1499938964844,
1033.426025390625,
1279.2193603515625,
21.837045669555664,
1498.863037109375,
30.5106201171875,
59.575592041015625,
34.36167526245117,
45.05063247680664,
23.87606430053711,
]

expert_return = 5383.310325177668
bc_return = 339.1794128417969

parser.add_argument('--env_name', type=str, required=True)
args = parser.parse_args()
params = vars(args)

fig,ax1 = plt.subplots(figsize=(10, 6))

# Plot line with error bars
ax1.errorbar(X, avg_return, yerr=std, 
             fmt='-o',         # Line and marker style
             color='blue',     # Color
             ecolor='lightblue', # Error bar color
             elinewidth=3,     # Error bar line width
             capsize=5,        # Error bar cap size
             label = 'DAgger'
             )

# add a second y axis for training loss
# ax2 = ax1.twinx()
# ax2.plot(
#     X, 
#     train_loss, 
#     '--s',  # Dashed line with square markers
#     color='red',
#     label=''
# )

# add horizontal lines
plt.axhline(y=expert_return, color='red', linestyle='--', linewidth=2, label='Expert')
plt.axhline(y=bc_return, color='green', linestyle='--', linewidth=2, label='BC')

# Customize plot
plt.title('DAgger Evaluation (with Std) for ' + params['env_name'], fontsize=14)
ax1.set_xlabel('Iteration', fontsize=12)
ax1.set_ylabel('Evaluation Average Return', fontsize=12)
# ax1.tick_params(axis='y', which='both', labelcolor='blue', color='blue')

# ax2.set_ylabel("Training Loss", fontsize=12, color='red')
# ax2.tick_params(axis='y', which='both', labelcolor='red', color='red')

plt.xticks(X)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# Add annotation for decreasing std
# plt.annotate('Standard Deviation Decreases\nwith More Training',
#              xy=(7, 1500), xytext=(4, 1000),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              fontsize=10)

plt.tight_layout()
plt.show()

