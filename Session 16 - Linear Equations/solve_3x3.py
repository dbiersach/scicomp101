# solve_3x3.py

import numpy as np

coeffs = np.array([[4, 5, -2], [7, -1, 2], [3, 1, 4]])
vals = np.array([-14, 42, 28])

det_Coeffs = np.linalg.det(coeffs)

arr_X = np.copy(coeffs)
arr_Y = np.copy(coeffs)
arr_Z = np.copy(coeffs)

arr_X[:, 0] = vals
arr_Y[:, 1] = vals
arr_Z[:, 2] = vals

det_X = np.linalg.det(arr_X)
det_Y = np.linalg.det(arr_Y)
det_Z = np.linalg.det(arr_Z)

x = det_X / det_Coeffs
y = det_Y / det_Coeffs
z = det_Z / det_Coeffs

print(f"x = {x:,.4f}")
print(f"y = {y:,.4f}")
print(f"z = {z:,.4f}")

print(np.linalg.inv(coeffs) @ vals)


