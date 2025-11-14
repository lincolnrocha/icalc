import numpy as np

class Calculator:
    
    def __init__(self):
        pass

    def add(self, a, b):
        return np.add(a, b)

    def sub(self, a, b):
        return np.subtract(a, b)

    def mut(self, a, b):
        return np.multiply(a, b)

    def div(self, a, b):
        if np.any(b == 0):
            raise ValueError("Division by zero is not allowed.")
        return np.divide(a, b)
