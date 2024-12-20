import numpy as np

def fitness(tree, X, Y):
    predictions = np.array([tree.evaluate(x) for x in X])
    mse = np.mean((predictions - Y) ** 2)
    return float(mse)