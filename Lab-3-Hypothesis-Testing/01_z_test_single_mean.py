# Large Sample Test for a Single Mean (Z-test)

import numpy as np
from scipy.stats import norm

data = [float(value) for value in input("Enter sample values separated by spaces: ").split()]
if not data:
    raise ValueError("Enter at least one sample value.")

mu0 = float(input("Enter hypothesized population mean (mu0): "))
sigma = float(input("Enter known population standard deviation (sigma): "))
alpha = float(input("Enter significance level (e.g. 0.05): "))
alternative = input("Alternative hypothesis (two-sided/less/greater): ").strip().lower()
if sigma <= 0 or not 0 < alpha < 1:
    raise ValueError("sigma must be positive and alpha must be between 0 and 1.")
if alternative not in ("two-sided", "less", "greater"):
    raise ValueError("Choose two-sided, less, or greater.")

n = len(data)
sample_mean = np.mean(data)
z = (sample_mean - mu0) / (sigma / np.sqrt(n))
if alternative == "two-sided":
    p_value = 2 * norm.sf(abs(z))
elif alternative == "greater":
    p_value = norm.sf(z)
else:
    p_value = norm.cdf(z)

print(f"\nSample size = {n}")
print(f"Sample mean = {sample_mean:.6f}")
print(f"Z statistic = {z:.6f}")
print(f"P-value = {p_value:.6f}")
print("Reject H0" if p_value <= alpha else "Fail to reject H0")
