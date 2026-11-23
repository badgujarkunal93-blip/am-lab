# Joint PMF for two fair dice, as in the practical sheet

import numpy as np
import matplotlib.pyplot as plt

outcomes = [1, 2, 3, 4, 5, 6]
probability = float(input("Enter probability for each equally likely pair (default 1/36): ") or (1 / 36))
if probability < 0:
    raise ValueError("Probability cannot be negative.")

pmf = np.full((6, 6), probability)
total = pmf.sum()
print(f"\nSum of all joint probabilities = {total:.6f}")
if not np.isclose(total, 1.0):
    print("Warning: the entered pair probability does not make a valid PMF (total must be 1).")

print("\nJoint PMF table (rows = die 1, columns = die 2):")
print(pmf)

plt.imshow(pmf, interpolation="nearest")
for i in range(6):
    for j in range(6):
        plt.text(j, i, f"{pmf[i, j]:.3f}", ha="center", va="center")
plt.title("Joint PMF of Two Dice")
plt.xlabel("Die 2")
plt.ylabel("Die 1")
plt.xticks(range(6), outcomes)
plt.yticks(range(6), outcomes)
plt.colorbar(label="Probability")
plt.show()
