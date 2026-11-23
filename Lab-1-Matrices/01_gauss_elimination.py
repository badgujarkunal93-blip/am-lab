# Gauss Elimination Method
# Enter the augmented matrix row by row. The last value in each row is the RHS.

n = int(input("Enter number of unknowns: "))
if n <= 0:
    raise ValueError("Number of unknowns must be positive.")

a = []
print(f"Enter {n} coefficients followed by the RHS for each equation:")
for i in range(n):
    row = [float(input(f"Row {i + 1}, value {j + 1}: ")) for j in range(n + 1)]
    a.append(row)

for i in range(n):
    pivot_row = max(range(i, n), key=lambda r: abs(a[r][i]))
    a[i], a[pivot_row] = a[pivot_row], a[i]

    if abs(a[i][i]) < 1e-12:
        raise ValueError("No unique solution exists (singular system).")

    for k in range(i + 1, n):
        factor = a[k][i] / a[i][i]
        for j in range(i, n + 1):
            a[k][j] -= factor * a[i][j]

print("\nUpper triangular matrix:")
for row in a:
    print([round(value, 4) for value in row])

x = [0.0] * n
for i in range(n - 1, -1, -1):
    total = sum(a[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (a[i][n] - total) / a[i][i]

print("\nSolution:")
for i, value in enumerate(x, start=1):
    print(f"x{i} = {value:.6g}")
