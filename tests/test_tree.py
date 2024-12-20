from src.tree import Node
import pytest


class TestTree():
    """Tests for the tree class."""
    
    def test_tree_evaluation_sum(self):
        tree = Node("+", Node("x"), Node(5))  # y = x + 5
        assert tree.evaluate(3) == 8  # 3 + 5 = 8
        assert tree.evaluate(0) == 5  # 0 + 5 = 5
        
    def test_tree_evaluation_sub(self):
        tree = Node("-", Node("x"), Node(5))  # y = x - 5
        assert tree.evaluate(3) == -2  # 3 - 5 = -2
        assert tree.evaluate(0) == -5  # 0 - 5 = -5
        
    def test_tree_evaluation_mul(self):
        tree = Node("*", Node("x"), Node(5))  # y = x * 5
        assert tree.evaluate(3) == 15  # 3 * 5 = 15
        assert tree.evaluate(0) == 0  # 0 * 5 = 0
        
    def test_tree_evaluation_div(self):
        tree = Node("/", Node("x"), Node(5))  # y = x / 5
        assert tree.evaluate(15) == 3  # 15 / 5 = 3
        assert tree.evaluate(0) == 0  # 0 / 5 = 0
        
    def test_tree_evaluation_mod(self):
        tree = Node("%", Node("x"), Node(5))  # y = x % 5
        assert tree.evaluate(15) == 0  # 15 % 5 = 0
        assert tree.evaluate(7) == 2  # 7 % 5 = 2
        
        
    def test_tree_evaluation_pow(self):
        tree = Node("^", Node("x"), Node(2))  # y = x ^ 2
        assert tree.evaluate(3) == 9  # 3 ^ 2 = 9
        assert tree.evaluate(0) == 0  # 0 ^ 2 = 0
        
    def test_tree_evaluation_sin(self):
        tree = Node("sin", Node("x"))  # y = sin(x)
        assert tree.evaluate(0) == 0  # sin(0) = 0
        assert tree.evaluate(3.14) == 0.0015926529164868282  # sin(3.14) = 0.0015926529164868282
        
    def test_tree_evaluation_cos(self):
        tree = Node("cos", Node("x"))  # y = cos(x)
        assert tree.evaluate(0) == 1  # cos(0) = 1
        assert tree.evaluate(3.14) == -0.9999987317275395  # cos(3.14) = -0.9999987317275395

    def test_tree_evaluation_pi(self):
        tree = Node("pi")  # y = pi
        assert tree.evaluate(0) == 3.141592653589793  # pi = 3.141592653589793
        
    def test_tree_evaluation_e(self):
        tree = Node("e")  # y = e
        assert tree.evaluate(0) == 2.718281828459045  # e = 2.718281828459045
        
    def test_tree_evaluation_sqrt(self):
        tree = Node("sqrt", Node("x"))  # y = sqrt(x)
        assert tree.evaluate(0) == 0  # sqrt(0) = 0
        assert tree.evaluate(9) == 3  # sqrt(9) = 3
        
    def test_tree_evaluation_number(self):
        tree = Node(5)  # y = 5
        assert tree.evaluate(0) == 5  # 5 = 5
        assert tree.evaluate(3) == 5  # 5 = 5

