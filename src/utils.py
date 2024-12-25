import random
import matplotlib.pyplot as plt
from src.tree import Node


def generate_random_tree(depth=3):
    """
    generate a random tree of a given depth
    """
    if depth <= 0:
        rnd = random.random()
        if rnd < 0.3:
            return Node("x")
        elif rnd < 0.4:
            return Node("pi")
        elif rnd < 0.5:
            return Node("e")
        else:
            return Node(str(random.randint(0, 10)))
    # randomly choose an operator
    operator = random.choice(["+", "-", "*", "/", "^", "sin", "cos", "sqrt"])
    if operator in ["sin", "cos", "sqrt"]:
        left = generate_random_tree(depth - 1)
        return Node(operator, left=left)
    left = generate_random_tree(depth - 1)
    right = generate_random_tree(depth - 1)
    return Node(operator, left=left, right=right)


def plot_mse_over_generations(mse_values):
    """
    plot the mean squared error over generations
    """
    plt.plot(mse_values)
    plt.xlabel("Generation")
    plt.ylabel("Mean Squared Error")
    plt.show()