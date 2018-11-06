#-*- coding: utf-8 -*-
import numpy as np

# A x = b

A = np.array([
    [2, 3, 12],
    [1, 1, 2],
    [2, 0, 3]
])

b = np.array([
    31,
    9,
    7
])

# x = A^-1 b

Ainv = np.linalg.inv(A)

x = np.matmul(Ainv, b)

print(x)

print(np.matmul(A, x))