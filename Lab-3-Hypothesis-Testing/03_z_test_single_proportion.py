# Large Sample Test for a Single Proportion

import math
from scipy.stats import norm

n = int(input("Enter sample size (n): "))
x = int(input("Enter number of successes (x): "))
p0 = float(input("Enter hypothesized population proportion (p0): "))
alpha = float(input("Enter significance level (e.g. 0.05): "))
tail = input("Enter test type (two/left/right): ").strip().lower()

if n <= 0 or not 0 <= x <= n or not 0 < p0 < 1 or not 0 < alpha < 1:
    raise ValueError("Check n, x, p0 and alpha values.")
if tail not in ("two", "left", "right"):
    raise ValueError("Tail must be two, left or right.")

phat = x / n
se = math.sqrt(p0 * (1 - p0) / n)
z = (phat - p0) / se
if tail == "two":
    p_value = 2 * norm.sf(abs(z))
elif tail == "right":
    p_value = norm.sf(z)
else:
    p_value = norm.cdf(z)

print(f"\nSample proportion = {phat:.6f}")
print(f"Population proportion under H0 = {p0:.6f}")
print(f"Calculated z = {z:.6f}")
print(f"P-value = {p_value:.6f}")
print("Reject H0" if p_value <= alpha else "Fail to reject H0")
