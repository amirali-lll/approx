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
        elif self.value == "^":
            base = self.left.evaluate(x)
            exponent = abs(self.right.evaluate(x))
            if base == 0:
                return 0
            if exponent == 0:
                return 1
            # check that the exponent is not very large to avoid overflow
            if exponent < 100 and exponent < 100 and exponent % 1 == 0:
                return base ** exponent
            return 1
            
        elif self.value == 'sin':
            left_val = self.left.evaluate(x)
            # check that the left_value is ok for the function
            return sin(left_val) if -10 <= left_val <= 10 else 0
        elif self.value == 'cos':
            left_val = self.left.evaluate(x)
            return cos(left_val) if -10 <= left_val <= 10 else 0
        elif self.value == 'tan':
            return tan(self.left.evaluate(x))
        elif self.value == 'pi':
            return pi
        elif self.value == 'e':
            return e
        elif self.value == 'sqrt':
            left_val = float(self.left.evaluate(x))
            return sqrt(left_val) if left_val >= 0 else 0
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
    
    def length(self):
        if self.left is None and self.right is None:
            return 1
        if self.right is None:
            return 1 + self.left.length()
        return 1 + self.left.length() + self.right.length()