# Simple Linear Regression using manual mean, slope and intercept calculations

import numpy as np
import matplotlib.pyplot as plt

x = np.array([float(value) for value in input("Enter X values separated by spaces: ").split()])
y = np.array([float(value) for value in input("Enter Y values separated by spaces: ").split()])
if len(x) != len(y) or len(x) < 2:
    raise ValueError("X and Y must have the same length (at least 2 values).")

x_mean = np.mean(x)
y_mean = np.mean(y)
denominator = np.sum((x - x_mean) ** 2)
if denominator == 0:
    raise ValueError("Slope is undefined because all X values are equal.")

slope = np.sum((x - x_mean) * (y - y_mean)) / denominator
intercept = y_mean - slope * x_mean
y_pred = intercept + slope * x

print(f"\nSlope (b) = {slope:.6f}")
print(f"Intercept (a) = {intercept:.6f}")
print(f"Regression equation: Y = {intercept:.6f} + {slope:.6f}X")
print("Predicted Y values:", y_pred)

plt.scatter(x, y, label="Actual data")
order = np.argsort(x)
plt.plot(x[order], y_pred[order], label="Regression line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
