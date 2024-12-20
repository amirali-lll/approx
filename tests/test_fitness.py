import numpy as np
from src.fitness import fitness
from src.tree import Node
import pytest 


@pytest.fixture
def tree():
    return Node('+', Node('x'), Node('1'))

def test_fitness_zero(tree):
    X = np.array([0, 1, 2, 3, 4])
    Y = np.array([1, 2, 3, 4, 5])
    assert fitness(tree, X, Y) == 0.0
    
def test_fitness_nonzero(tree):
    X = np.array([0, 1, 2, 3, 4])
    Y = np.array([0, 1, 2, 3, 4])
    assert fitness(tree, X, Y) == 1.0
    
    
