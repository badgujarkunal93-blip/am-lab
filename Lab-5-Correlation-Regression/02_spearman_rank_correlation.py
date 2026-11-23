# Spearman's Rank Correlation
# Average ranks are used for tied values; Pearson correlation is then calculated on ranks.

import numpy as np
from scipy.stats import rankdata

x = np.array([float(value) for value in input("Enter X values separated by spaces: ").split()])
y = np.array([float(value) for value in input("Enter Y values separated by spaces: ").split()])
if len(x) != len(y) or len(x) < 2:
    raise ValueError("X and Y must have the same length (at least 2 values).")

rank_x = rankdata(x)
rank_y = rankdata(y)
rho = np.corrcoef(rank_x, rank_y)[0, 1]
print("Ranks of X:", rank_x)
print("Ranks of Y:", rank_y)
print(f"Spearman's rank correlation (rho) = {rho:.4f}")
