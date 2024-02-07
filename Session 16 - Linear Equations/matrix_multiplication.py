# matrix_multiplication.py

import numpy as np

a = np.array([[4, 5, 8], [1, 9, 7]])
print(f"A = {a}")
print(f"Shape of A: {a.shape}\n")

b = np.array([[2, 4], [6, 1], [5, 9]])
print(f"B = {b}")
print(f"Shape of B: {b.shape}\n")

c = np.matmul(a, b)
print(f"C = {c}")
print(f"Shape of C: {c.shape}\n")

c = np.matmul(b, a)
print(f"C = {c}")
print(f"Shape of C: {c.shape}\n")

a = np.array([[4, 5, 8], [1, 9, 7], [0, 0, 0]])
print(f"A = {a}")
print(f"Shape of A: {a.shape}\n")

c = np.matmul(b, a)
