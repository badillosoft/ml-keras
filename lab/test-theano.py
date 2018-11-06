import theano
import theano.tensor as T

x, y = T.scalars("x", "y")

z = T.exp(-x ** 2 - y ** 2)

norm = theano.function([x, y], z)

print(norm(2, 2))