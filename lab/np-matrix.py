import tensorflow as tf
import numpy as np

A = np.array([
    [1, 2],
    [1, 3]
])

b = np.array([
    [1],
    [2]
])

print(A)
print(b)

C = np.matmul(A, b)

print(C)