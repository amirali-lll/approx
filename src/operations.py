import random
from src.tree import Node
from src.utils import generate_random_tree
from src.conf import MUTATION_PROBABILITY


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