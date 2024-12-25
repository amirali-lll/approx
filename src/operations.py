import random
from src.tree import Node
from src.utils import generate_random_tree
from src.conf import MUTATION_PROBABILITY
from src.fitness import fitness
import copy



def mutate(tree, depth=3):
    """
    mutate a tree by replacing a random node with a new random tree
    """
    if random.random() < MUTATION_PROBABILITY:
        tree = generate_random_tree(depth)
    if tree.left:
        tree.left = mutate(tree.left, depth - 1)
    if tree.right:
        tree.right = mutate(tree.right, depth - 1)
    return tree



def reproduce(tree1, tree2):
    """
    crossover two trees by swapping random subtrees
    """
    if tree1 is None:
        return copy.deepcopy(tree2)
    if tree2 is None:
        return copy.deepcopy(tree1)
    if random.random() < 0.5:
        value = tree1.value
        right = copy.deepcopy(tree1.right)
        left = copy.deepcopy(tree1.left)
    else:
        value = tree2.value
        right = copy.deepcopy(tree2.right)
        left = copy.deepcopy(tree2.left)
    return Node(value, left=left, right=right)


def prune(tree, x_values, y_values):
    """
    prune a tree by removing subtrees that do not improve the fitness
    """
    if tree.left and tree.right:
        left_fitness = fitness(tree.left, x_values, y_values)
        right_fitness = fitness(tree.right, x_values, y_values)
        tree_fitness = fitness(tree, x_values, y_values)
        if left_fitness > tree_fitness and right_fitness > tree_fitness:
            return tree
        if left_fitness > right_fitness:
            return tree.left
        return tree.right
    return tree