import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    return np.square(x)

def is_feasible(x):
    g = x - 5
    return g <= 0

# TODO: Implement your own EA to minimize the objective function