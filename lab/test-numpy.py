import numpy as np

x = np.linspace(-np.pi, np.pi, 11)
y = np.sin(x)

print(x)
print(y)

vec = np.arange(1, 5)

print(vec)

vec2 = vec.reshape((-1, 1))

print(vec2)

vec3 = vec2.reshape(len(vec))

print(vec3)

r = np.random.randn(4)

print (r)

r2 = np.random.randn(4, 2)

print (r2)

s = np.random.random_sample(4)

print(s)

s2 = np.random.random_sample((4, 2))

print(s2)