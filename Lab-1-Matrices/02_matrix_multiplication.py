# Matrix Multiplication

r1 = int(input("Rows in matrix A: "))
c1 = int(input("Columns in matrix A: "))
r2 = int(input("Rows in matrix B: "))
c2 = int(input("Columns in matrix B: "))

if min(r1, c1, r2, c2) <= 0:
    raise ValueError("Matrix dimensions must be positive.")
if c1 != r2:
    raise ValueError("Multiplication is not possible: columns of A must equal rows of B.")

print("\nEnter matrix A:")
A = [[float(input(f"A[{i + 1}][{j + 1}]: ")) for j in range(c1)] for i in range(r1)]
print("\nEnter matrix B:")
B = [[float(input(f"B[{i + 1}][{j + 1}]: ")) for j in range(c2)] for i in range(r2)]

result = [[0.0 for _ in range(c2)] for _ in range(r1)]
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j] += A[i][k] * B[k][j]

print("\nProduct matrix A x B:")
for row in result:
    print([round(value, 4) for value in row])
