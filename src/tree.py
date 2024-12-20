from math import sin, cos, tan, pi, e, sqrt

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def evaluate(self, x):
        if self.value == 'x':
            return x
        elif self.value == '+':
            return self.left.evaluate(x) + self.right.evaluate(x)
        elif self.value == '-':
            return self.left.evaluate(x) - self.right.evaluate(x)
        elif self.value == '*':
            return self.left.evaluate(x) * self.right.evaluate(x)
        elif self.value == '/':
            right_val = self.right.evaluate(x)
            return self.left.evaluate(x) / right_val if right_val != 0 else 1
        elif self.value == '%':
            return self.left.evaluate(x) % self.right.evaluate(x)
        elif self.value == '^':
            return self.left.evaluate(x) ** self.right.evaluate(x)
        elif self.value == 'sin':
            return sin(self.left.evaluate(x))
        elif self.value == 'cos':
            return cos(self.left.evaluate(x))
        elif self.value == 'tan':
            return tan(self.left.evaluate(x))
        elif self.value == 'pi':
            return pi
        elif self.value == 'e':
            return e
        elif self.value == 'sqrt':
            return sqrt(self.left.evaluate(x))
        else:
            return float(self.value)

    def __str__(self):
        if self.value in ['x', 'pi', 'e']:
            return self.value
        elif self.value in ['sin', 'cos', 'tan', 'sqrt']:
            return f"{self.value}({self.left})"
        elif self.value in ['+', '-', '*', '/', '%', '^']:
            return f"({self.left} {self.value} {self.right})"
        else:
            return self.value
        
