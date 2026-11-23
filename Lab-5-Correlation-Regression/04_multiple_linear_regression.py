# Multiple Linear Regression using the Normal Equation
# Enter one row of predictor values per observation, then the corresponding Y value.

import numpy as np

n = int(input("Enter number of observations: "))
p = int(input("Enter number of independent variables: "))
if n <= 0 or p <= 0 or n < p + 1:
    raise ValueError("Need positive dimensions and at least p + 1 observations.")

X_rows = []
y_values = []
for i in range(n):
    print(f"\nObservation {i + 1}")
    row = [float(input(f"X{j + 1}: ")) for j in range(p)]
    target = float(input("Y: "))
    X_rows.append(row)
    y_values.append(target)

X = np.array(X_rows, dtype=float)
y = np.array(y_values, dtype=float)
X_design = np.column_stack((np.ones(n), X))

# Least-squares solution is numerically safer than directly inverting X transpose X.
coefficients, residuals, rank, singular_values = np.linalg.lstsq(X_design, y, rcond=None)
if rank < p + 1:
    print("Warning: predictors are linearly dependent; a least-squares solution is returned.")

intercept = coefficients[0]
slopes = coefficients[1:]
print(f"\nIntercept (a) = {intercept:.6f}")
for i, coefficient in enumerate(slopes, start=1):
    print(f"Coefficient b{i} = {coefficient:.6f}")

terms = [f"{intercept:.4f}"] + [f"({slopes[i]:.4f} * X{i + 1})" for i in range(p)]
print("Regression equation: Y = " + " + ".join(terms))

print("\nEnter predictor values for a new prediction:")
new_values = [float(input(f"X{i + 1}: ")) for i in range(p)]
prediction = intercept + np.dot(slopes, new_values)
print(f"Predicted Y = {prediction:.6f}")
