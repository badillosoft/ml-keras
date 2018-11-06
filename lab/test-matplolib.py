import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 2, 3])

plt.savefig("g.png")

plt.clf()

import numpy as np

n = np.random.normal(4, 2, 1000)

plt.hist(n, bins=10)

plt.savefig("g2.png")