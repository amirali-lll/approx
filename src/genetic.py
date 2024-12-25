import copy
import random
from src.operations import mutate, reproduce, prune

from src.fitness import fitness
from src.utils import generate_random_tree
from src.conf import DEFAULT_POPULATION_SIZE, DEFAULT_GENERATIONS


def genetic_programming(x_values, y_values, population_size=DEFAULT_POPULATION_SIZE, generations=DEFAULT_GENERATIONS):
    """Run the genetic programming algorithm."""
    population = [generate_random_tree() for _ in range(population_size)]
    mse_values = []

    for generation in range(generations):
        print(f"{generation}/{generations}", end="\r")
        sorted_population = sorted(population, key=lambda tree: fitness(tree, x_values, y_values))


        mse_values.append(fitness(sorted_population[0], x_values, y_values))
        
        # peaking the 20% best trees, 30% peek randomly, 50% reproduce for the next generation and one deep copy of the best tree
        next_generation = [copy.deepcopy(sorted_population[0])]
        next_generation.extend(sorted_population[:int(0.2 * population_size)])
        next_generation.extend(random.choices(sorted_population[int(0.2 * population_size):], k=int(0.3 * population_size)))
        
        # reproduce the others by peeking parents randomly
        while len(next_generation) < population_size:
            parent1 = random.choice(sorted_population)
            parent2 = random.choice(sorted_population)
            next_generation.append(reproduce(parent1, parent2))
        
        # mutate the trees except the best one
        for i in range(1, population_size):
            next_generation[i] = mutate(next_generation[i])
            
        # prune the trees
        for tree in next_generation:
            tree = prune(tree, x_values, y_values)
        
        population = next_generation
            

    return sorted_population[0], mse_values
