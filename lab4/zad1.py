import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np
import math


def endurance(lista):
    if len(lista) != 6:
        print("Error: List length not equal to 6")
    else:
        x, y, z, u, v, w = lista[0], lista[1], lista[2], lista[3], lista[4], lista[5]
        return -(math.exp(-2 * (y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w))


def f(x):
    j = [endurance(x[i]) for i in range(len(x))]
    return np.array(j)


options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)

optimizer = ps.single.GlobalBestPSO(
    n_particles=10, dimensions=6, options=options, bounds=my_bounds)

optimizer.optimize(f, iters=1000)
