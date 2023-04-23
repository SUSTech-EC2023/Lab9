import numpy as np
import matplotlib.pyplot as plt

# Define the objective function and constraints
def objective_function(x):
    return (x[0] - 4) ** 2 + (x[1] - 4) ** 2

def constraint1(x):
    return x[0] + x[1] - 6

def constraint2(x):
    return 5 - x[0] - x[1]

def constraint_function(x):
    return [constraint1(x), constraint2(x)]

# TODO: Implement your own EA to minimize the objective function
