# F-test for Comparison of Two Variances (two-tailed)

from scipy.stats import f

sample1 = [float(value) for value in input("Enter sample 1 values separated by spaces: ").split()]
sample2 = [float(value) for value in input("Enter sample 2 values separated by spaces: ").split()]
alpha = float(input("Enter significance level (e.g. 0.05): "))
if len(sample1) < 2 or len(sample2) < 2:
    raise ValueError("Each sample must contain at least two values.")
if not 0 < alpha < 1:
    raise ValueError("alpha must be between 0 and 1.")

def sample_variance(values):
    mean = sum(values) / len(values)
    return sum((value - mean) ** 2 for value in values) / (len(values) - 1)

var1 = sample_variance(sample1)
var2 = sample_variance(sample2)
if var1 == 0 or var2 == 0:
    raise ValueError("Both sample variances must be positive.")

if var1 >= var2:
    f_stat = var1 / var2
    df1, df2 = len(sample1) - 1, len(sample2) - 1
else:
    f_stat = var2 / var1
    df1, df2 = len(sample2) - 1, len(sample1) - 1

p_value = min(1.0, 2 * f.sf(f_stat, df1, df2))
print(f"\nMean 1 = {sum(sample1) / len(sample1):.6f}")
print(f"Mean 2 = {sum(sample2) / len(sample2):.6f}")
print(f"Variance 1 = {var1:.6f}")
print(f"Variance 2 = {var2:.6f}")
print(f"F statistic (larger variance / smaller variance) = {f_stat:.6f}")
print(f"Degrees of freedom = ({df1}, {df2})")
print(f"P-value = {p_value:.6f}")
print("Reject H0" if p_value <= alpha else "Fail to reject H0")
