#-*- coding: utf-8 -*-
import numpy as np

## Generación de Vectores

# 1. Generar un vector de 10 elementos del 1 al 10
vec1 = np.arange(1, 11) # El último no lo toca [a, b)

print(vec1)

# 2. Generar un vector de 10 ceros
vec2 = np.zeros(10)

print(vec2)

# 3. Generar un vector de 10 unos
vec3 = np.ones(10)

print(vec3)

# 4. Generar un vector con 10 aleatorios del [0, 1)
vec4 = np.random.rand(10)

print(vec4)

# 5. Generar un vector con 10 aleatorios bajo
# la distribuición normal con p=2 y ds=0.774
vec5 = np.random.normal(2, 0.774, 10)

print(vec5)

# 6. Generar un vector de 10 aleatorios en
# el rango de a=-pi a b=pi
a = -np.pi
b = np.pi
vec6 = (b - a) * np.random.random_sample(10) + a

print(vec6)

## Operaciones entre Vectores

a = np.array([1, 2, 3])
b = np.array([1, 3, 5])

print("a: {}".format(a))
print("b: {}".format(b))

# 1. Suma de vectores
r = a + b

print("a + b: {}".format(r))

# 2. Resta de vectores
r = a - b

print("a - b: {}".format(r))

# 3. Multiplicar/Dividir vectores y escalares
r = a * 5

print("a * 5: {}".format(r))

r = 5 * a

print("5 * a: {}".format(r))

r = a / 2.

print("a / 2: {}".format(r))

r = 2. / a

print("2 / a: {}".format(r))

# 4. Multiplicación directa entre vectores
r = a * b

print("a * b: {}".format(r))

# 5. Producto interno (producto punto)
s = np.dot(a, b)

print("a . b: {}".format(s))

s = np.dot([1, 2], [-2, 1])

print("a . b: {}".format(s))