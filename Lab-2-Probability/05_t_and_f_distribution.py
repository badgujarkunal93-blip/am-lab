# Generate random samples from Student's t and F distributions using normal variables

import numpy as np
import matplotlib.pyplot as plt

df_t = int(input("Enter degrees of freedom for t distribution: "))
df1 = int(input("Enter numerator degrees of freedom for F distribution: "))
df2 = int(input("Enter denominator degrees of freedom for F distribution: "))
number = int(input("Enter number of random samples (suggested 5000): "))
if min(df_t, df1, df2, number) <= 0:
    raise ValueError("Degrees of freedom and sample count must be positive.")

def t_random(df):
    z = np.random.normal(0, 1)
    v = sum(np.random.normal(0, 1) ** 2 for _ in range(df))
    return z / np.sqrt(v / df)

def f_random(d1, d2):
    u = sum(np.random.normal(0, 1) ** 2 for _ in range(d1)) / d1
    v = sum(np.random.normal(0, 1) ** 2 for _ in range(d2)) / d2
    return u / v

t_samples = [t_random(df_t) for _ in range(number)]
f_samples = [f_random(df1, df2) for _ in range(number)]

plt.figure(figsize=(11, 5))
plt.subplot(1, 2, 1)
plt.hist(t_samples, bins=60, density=True, edgecolor="black")
plt.title(f"Student's t Distribution (df={df_t})")
plt.xlabel("Value")
plt.ylabel("Density")

plt.subplot(1, 2, 2)
plt.hist(f_samples, bins=60, density=True, edgecolor="black")
plt.title(f"F Distribution (df1={df1}, df2={df2})")
plt.xlabel("Value")
plt.ylabel("Density")
plt.tight_layout()
plt.show()
