import numpy as np
from src.genetic import genetic_programming
from src.utils import plot_mse_over_generations

def main():
    x_values = np.linspace(-10, 10, 200)
    y_values = x_values**2 + 3 * x_values + 2
    best_tree, mse_values = genetic_programming(x_values, y_values)
    print(f"Best tree: {best_tree}")
    print(f"Best tree MSE: {mse_values[-1]}")
    print(f"Length of MSE values: {len(mse_values)}")
    plot_mse_over_generations(mse_values)

if __name__ == "__main__":
    main()
