# Eigenvalues, Eigenvectors and Diagonalization of a 2 x 2 Matrix
# Uses the characteristic equation: lambda^2 - trace(A)*lambda + det(A) = 0.

import math

a = float(input("Enter a11: "))
b = float(input("Enter a12: "))
c = float(input("Enter a21: "))
d = float(input("Enter a22: "))

trace = a + d
det = a * d - b * c
discriminant = trace ** 2 - 4 * det

if discriminant < -1e-12:
    print("This practical's manual method supports real eigenvalues only.")
else:
    root = math.sqrt(max(0.0, discriminant))
    eigenvalues = [(trace + root) / 2, (trace - root) / 2]
    print("\nEigenvalues:", eigenvalues)

    vectors = []
    for lam in eigenvalues:
        # Solve (A - lambda I)v = 0 using the more stable available row.
        if abs(b) > 1e-12:
            vector = [1.0, -(a - lam) / b]
        elif abs(c) > 1e-12:
            vector = [-(d - lam) / c, 1.0]
        elif abs(a - lam) > 1e-12:
            vector = [0.0, 1.0]
        else:
            vector = [1.0, 0.0]
        vectors.append(vector)
        print(f"Eigenvector for lambda = {lam:.6g}: {vector}")

    p = [[vectors[0][0], vectors[1][0]],
         [vectors[0][1], vectors[1][1]]]
    det_p = p[0][0] * p[1][1] - p[0][1] * p[1][0]

    print("\nP matrix:")
    for row in p:
        print(row)

    if abs(det_p) < 1e-12:
        print("P is singular, so this matrix cannot be diagonalized using these eigenvectors.")
    else:
        p_inv = [[p[1][1] / det_p, -p[0][1] / det_p],
                 [-p[1][0] / det_p, p[0][0] / det_p]]
        ap = [[a * p[0][0] + b * p[1][0], a * p[0][1] + b * p[1][1]],
              [c * p[0][0] + d * p[1][0], c * p[0][1] + d * p[1][1]]]
        diagonal = [
            [p_inv[0][0] * ap[0][0] + p_inv[0][1] * ap[1][0],
             p_inv[0][0] * ap[0][1] + p_inv[0][1] * ap[1][1]],
            [p_inv[1][0] * ap[0][0] + p_inv[1][1] * ap[1][0],
             p_inv[1][0] * ap[0][1] + p_inv[1][1] * ap[1][1]]
        ]
        print("\nP inverse:")
        for row in p_inv:
            print(row)
        print("\nD = P inverse x A x P:")
        for row in diagonal:
            print([round(value, 6) for value in row])
