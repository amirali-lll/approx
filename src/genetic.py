import numpy as np
import random
from src.operations import mutate
from src.fitness import fitness
from src.utils import generate_random_tree
from src.conf import DEFAULT_POPULATION_SIZE, DEFAULT_GENERATIONS

def genetic_programming(x_values, y_values, population_size=DEFAULT_POPULATION_SIZE, generations=DEFAULT_GENERATIONS):
    """Run the genetic programming algorithm."""
    # Step 1: Initialize population
    population = [generate_random_tree() for _ in range(population_size)]
    mse_values = []

    for generation in range(generations):
        # Step 2: Evaluate fitness
        fitness_scores = [fitness(tree, x_values, y_values) for tree in population]

        # Step 3: Sort population by fitness scores explicitly
        population_with_scores = list(zip(fitness_scores, population))
        sorted_population_with_scores = sorted(population_with_scores, key=lambda item: item[0])
        sorted_population = [tree for _, tree in sorted_population_with_scores]

        # Logging best fitness
        best_index = 0  # Best tree is now the first one after sorting
        mse_values.append(sorted_population_with_scores[best_index][0])
        print(f"Generation {generation}, Best MSE: {mse_values[-1]}")

        # Step 4: Select the top individuals (elitism)
        population = sorted_population[: population_size // 2]

        # Step 5: Reproduce (add mutated and crossover individuals)
        while len(population) < population_size:
            parent = random.choice(population)
            child = mutate(parent)
            population.append(child)

    # Return the best tree and the MSE progression
    return sorted_population[0], mse_values
