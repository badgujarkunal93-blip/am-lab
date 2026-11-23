# Central Limit Theorem simulation using a uniform population, as in the lab code

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

sample_size = int(input("Enter sample size: "))
num_samples = int(input("Enter number of samples: "))
population_size = int(input("Enter population size (suggested 100000): "))
if min(sample_size, num_samples, population_size) <= 0:
    raise ValueError("All sizes must be positive.")
if sample_size > population_size:
    raise ValueError("Sample size cannot exceed population size when sampling without replacement.")

population = np.random.uniform(0, 1, population_size)
sample_means = []
for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=True)
    sample_means.append(np.mean(sample))

mean = np.mean(sample_means)
std = np.std(sample_means)
print(f"Mean of sample means = {mean:.6f}")
print(f"Standard deviation of sample means = {std:.6f}")

plt.figure(figsize=(11, 5))
plt.subplot(1, 2, 1)
plt.hist(population, bins=50, density=True, edgecolor="black")
plt.title("Original Uniform Population")
plt.xlabel("Value")
plt.ylabel("Density")

plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=40, density=True, edgecolor="black")
x = np.linspace(min(sample_means), max(sample_means), 500)
if std > 0:
    plt.plot(x, norm.pdf(x, mean, std), label="Normal curve")
plt.title("Sampling Distribution of Means")
plt.xlabel("Sample mean")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()
