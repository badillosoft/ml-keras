import numpy as np

A = np.array([
    [1, 1],
    [1, 2]
])

b = np.array([
    3,
    5
])

x = np.linalg.solve(A, b)

print(x)

d = np.linalg.det(A)
A_inv = np.linalg.inv(A)
B = b.reshape(-1, 1)
X = np.matmul(A_inv, B) / d
x = X.reshape(len(b))

print(d)
print(A_inv)
print(x)