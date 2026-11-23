# Inverse of a 2 x 2 Matrix

a = float(input("Enter a11: "))
b = float(input("Enter a12: "))
c = float(input("Enter a21: "))
d = float(input("Enter a22: "))

det = a * d - b * c
print(f"\nDeterminant = {det:.6g}")

if abs(det) < 1e-12:
    print("The matrix is singular; inverse does not exist.")
else:
    inverse = [[d / det, -b / det], [-c / det, a / det]]
    print("Inverse matrix:")
    for row in inverse:
        print([round(value, 6) for value in row])
