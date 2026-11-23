# Small Sample t-test for Difference of Means (pooled variance, two-tailed)

import math
from scipy.stats import t

sample1 = [float(value) for value in input("Enter values for sample 1 separated by spaces: ").split()]
sample2 = [float(value) for value in input("Enter values for sample 2 separated by spaces: ").split()]
alpha = float(input("Enter significance level (e.g. 0.05): "))
if len(sample1) < 2 or len(sample2) < 2:
    raise ValueError("Each sample must contain at least two values.")
if not 0 < alpha < 1:
    raise ValueError("alpha must be between 0 and 1.")

n1, n2 = len(sample1), len(sample2)
mean1, mean2 = sum(sample1) / n1, sum(sample2) / n2
var1 = sum((x - mean1) ** 2 for x in sample1) / (n1 - 1)
var2 = sum((x - mean2) ** 2 for x in sample2) / (n2 - 1)
sp = math.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
if sp == 0:
    raise ValueError("Pooled standard deviation is zero; t statistic is undefined.")

t_value = (mean1 - mean2) / (sp * math.sqrt(1 / n1 + 1 / n2))
df = n1 + n2 - 2
p_value = 2 * t.sf(abs(t_value), df)

print(f"\nMean 1 = {mean1:.6f}")
print(f"Mean 2 = {mean2:.6f}")
print(f"Variance 1 = {var1:.6f}")
print(f"Variance 2 = {var2:.6f}")
print(f"Pooled SD = {sp:.6f}")
print(f"t statistic = {t_value:.6f}")
print(f"Degrees of freedom = {df}")
print(f"P-value = {p_value:.6f}")
print("Reject H0" if p_value <= alpha else "Fail to reject H0")
