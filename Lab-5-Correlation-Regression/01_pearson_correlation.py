# Karl Pearson's Coefficient of Correlation

import numpy as np

x = np.array([float(value) for value in input("Enter X values separated by spaces: ").split()])
y = np.array([float(value) for value in input("Enter Y values separated by spaces: ").split()])
if len(x) != len(y) or len(x) < 2:
    raise ValueError("X and Y must have the same length (at least 2 values).")

mean_x = np.mean(x)
mean_y = np.mean(y)
numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sqrt(np.sum((x - mean_x) ** 2) * np.sum((y - mean_y) ** 2))
if denominator == 0:
    raise ValueError("Correlation is undefined when either variable has zero variation.")

r = numerator / denominator
print(f"Karl Pearson's coefficient of correlation (r) = {r:.4f}")
