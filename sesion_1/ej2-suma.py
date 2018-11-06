# Creamos una lista llamada x con algunos valores
x = [1, 6, 3, 4, 2, 7, 8, 5]

# Obtenemos la suma de la lista x
s = sum(x)

# Obtenemos el numero de elmentos en la lista x
n = len(x)

# Calculamos el promedio que es la suma de los elementos
# dividida entre el numero de elementos
# convertimos la suma en decimal para que la division
# no sea entera (1 / 2 = 0) pero (1.0 / 2 = 0.5)
p = float(s) / n

# Obtenemos el elemento minimo de la lista x
minx = min(x)

# Obtenemos el elemento maximo de la lista x
maxx = max(x)

print("Lista: {}".format(x))
print("Suma: {}".format(s))
print("Promedio: {}".format(p))
print("Minimo: {}".format(minx))
print("Maximo: {}".format(maxx))