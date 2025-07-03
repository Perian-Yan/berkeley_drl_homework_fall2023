import numpy as np
import matplotlib.pyplot as plt

X = [50, 100, 150, 200]
avg_return = [454.58, 342.12, 437.74, 652.06]
train_loss = [0.073, 0.061, 0.056, 0.0495]
std = [295.67, 301.93, 446.44, 813.36]

fig,ax1 = plt.subplots(figsize=(10, 6))

# Plot line with error bars
ax1.errorbar(X, avg_return, yerr=std, 
             fmt='-o',         # Line and marker style
             color='blue',     # Color
             ecolor='lightblue', # Error bar color
             elinewidth=3,     # Error bar line width
             capsize=5,        # Error bar cap size
             label = ''
             )

ax2 = ax1.twinx()
ax2.plot(
    X, 
    train_loss, 
    '--s',  # Dashed line with square markers
    color='red',
    label=''
)

# Customize plot
plt.title('Behavioral Cloning Evaluation (with Std)', fontsize=14)
ax1.set_xlabel('Train Batch Size', fontsize=12)
ax1.set_ylabel('Evaluation Average Return', fontsize=12, color='blue')
ax2.set_ylabel("Training Loss", fontsize=12, color='red')
ax1.tick_params(axis='y', which='both', labelcolor='blue', color='blue')
ax2.tick_params(axis='y', which='both', labelcolor='red', color='red')
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

