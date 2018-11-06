import numpy as np

x = np.array([2.77146031, 1.26693588, 3.17842508, 1.60157907, 1.46154484, 2.14581999,
 1.54197684, 1.72506751, 2.61465335, 1.5647302])

print("Tipo: {}".format(type(x)))
print("Arreglo: {}".format(x))

p = sum(x) / len(x)

print("Promedio: {}".format(p))

n = len(x)

s2 = (1. / (n - 1)) * sum((x - p) ** 2)

print("Varianza: {}".format(s2))

s = s2 ** 0.5

print("Desviacion estandar: {}".format(s))