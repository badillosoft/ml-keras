x = [1, 2, 2, 2, 3, 1, 2, 2, 3, 3, 1]

p = float(sum(x)) / len(x)

print("Tipo: {}".format(type(x)))
print("Lista: {}".format(x))
print("Promedio: {}".format(p))

l = [(xi - p) ** 2 for xi in x]

print("Cuadrados: {}".format(l))

n = len(x)

s2 = sum(l) / (n - 1)

print("Varianza: {}".format(s2))

s = s2 ** 0.5

print("Desviacion estandar: {}".format(s))