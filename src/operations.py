import random
from src.tree import Node
from src.utils import generate_random_tree
from src.conf import MUTATION_PROBABILITY
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