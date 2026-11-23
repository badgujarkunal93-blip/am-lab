# Binomial Distribution: calculate P(X = k) for every k from 0 to n

import math
import matplotlib.pyplot as plt

n = int(input("Enter number of trials (n): "))
p = float(input("Enter probability of success (p): "))
if n < 0 or not 0 <= p <= 1:
    raise ValueError("n must be non-negative and p must be between 0 and 1.")

values = list(range(n + 1))
probabilities = [
    math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    for k in values
]

print(f"\nBinomial Distribution (n={n}, p={p})")
print("k\tP(X=k)")
for k, probability in zip(values, probabilities):
    print(f"{k}\t{probability:.6f}")

plt.bar(values, probabilities, edgecolor="black")
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.xlabel("Number of successes (k)")
plt.ylabel("P(X = k)")
plt.xticks(values)
plt.grid(axis="y", alpha=0.3)
plt.show()
