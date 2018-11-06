#-*- coding: utf-8 -*-
import numpy as np

# Generación de matrices

# 1. Generar una matriz de 2x2
mat1 = np.array([
    [1, 2],
    [2, 1]
])

print(mat1)

# 2. Generar una matriz de 3x5
mat2 = np.array([
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [1, 3, 5, 2, 4],
    [2, 4, 5, 3, 1]
])

print(mat2)

# 3. Convertir un vector en matriz
vec = np.array([1, 2, 3, 4, 5, 6])
dim = (3, 2)
mat3 = vec.reshape(dim)

print(mat3)

# 4. Convertir una matriz en un vector
vec2 = mat3.reshape(6)

print(vec2)

dim = (1, 6)
mat4 = mat3.reshape(dim)

print(mat4)

# 4. Generar una matriz de nxm en un rango (1 al 121)
n = 10
m = 12
dim = (n, m)
mat5 = np.arange(n * m).reshape(dim)

print(mat5)

# 5. Generar un tensor a partir de un arreglo
vec = np.array([1, 2, 3, 4, 5, 6, 7, 8])

dim = (2, 2, 2)
t1 = vec.reshape(dim)

print(t1)

dim = (8)
vec2 = t1.reshape(dim)

print(vec2)

dim = (4, 2)
mat6 = vec2.reshape(dim)

print(mat6)

# Vector - Matriz - Vector (Vector Fila / Vector Columna)

vec = np.array([1, 2, 3]) # (1, 2, 3)

vecc = vec.reshape((3, 1)) # ((1), (2), (3))
vecf = vec.reshape((1, 3)) # ((1, 2, 3))

print(vec)
print(vecc)
print(vecf)

A = np.array([
    [1, 2, 3],
    [5, 4, 6],
    [9, 8, 7]
])

r = np.matmul(vecf, A)

print("R: {}".format(r))

x = np.array([0.2, 0.5, -0.1])
xf = x.reshape((3, 1))
xc = x.reshape((1, 3))
A = np.array([
    [1, 3, 5],
    [4, 5, 6],
    [7, 9, 11]
])

r = np.matmul(xc, np.matmul(A, xf))

print(r)