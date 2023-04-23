import numpy as np
import matplotlib.pyplot as plt

# Define the objective function and constraints
def objective_function(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2

# Constraints
def constraint1(x):
    return (x[0] - 1)**2 + (x[1] - 1)**2 - 1

def constraint2(x):
    return (x[0] - 4)**2 + (x[1] - 4)**2 - 1

def constraint3(x):
    return (x[0] - 1)**2 + (x[1] - 5)**2 - 1

def constraint_function(x):
    return [constraint1(x), constraint2(x), constraint3(x)]

# TODO: Implement your own EA to minimize the objective function
