import numpy as np
from src.conf import LENGTH_PENALTY

def fitness(tree, X, Y):
    predictions = np.array([tree.evaluate(x) for x in X])
    mse = np.mean((predictions - Y) ** 2)

    mse += tree.length() / LENGTH_PENALTY
    
    return float(mse)