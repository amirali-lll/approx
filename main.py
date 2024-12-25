import numpy as np
from src.genetic import genetic_programming
from src.utils import plot_mse_over_generations

def main():
    x_values = np.linspace(-10, 10, 100)
    y_values = x_values**4 + 5 * x_values + 8
    best_tree, mse_values = genetic_programming(x_values, y_values)
    print(f"Best tree: {best_tree}")
    print(f"Best tree MSE: {mse_values[-1]}")
    print(f"Length of MSE values: {len(mse_values)}")
    print(f"Accuracy: {accuracy(mse_values[-1], y_values)}")
    plot_mse_over_generations(mse_values)


# define the accuracy of the program : 1 - MSE / (variance of true outputs)
def accuracy(mse, y_values):
    return 1 - mse / np.var(y_values)


if __name__ == "__main__":
    main()
