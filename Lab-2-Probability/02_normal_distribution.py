# Normal Distribution PDF using the mathematical formula

import math
import numpy as np
import matplotlib.pyplot as plt

mu = float(input("Enter mean (mu): "))
sigma = float(input("Enter standard deviation (sigma): "))
if sigma <= 0:
    raise ValueError("Standard deviation must be positive.")

x = float(input("Enter x value to calculate density: "))
density = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(
    -((x - mu) ** 2) / (2 * sigma ** 2)
)
print(f"Normal probability density at x={x}: {density:.8f}")
print("Note: PDF density at one point is not the probability of that exact value.")

x_values = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 500)
pdf_values = [
    (1 / (sigma * math.sqrt(2 * math.pi))) *
    math.exp(-((value - mu) ** 2) / (2 * sigma ** 2))
    for value in x_values
]
plt.plot(x_values, pdf_values, label=f"N({mu}, {sigma ** 2})")
plt.title("Normal Distribution PDF")
plt.xlabel("x")
plt.ylabel("Probability density")
plt.grid(True)
plt.legend()
plt.show()
