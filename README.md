# Simple Caculator

`Calculator`s API.

```python
import numpy as np

class Calculator:

    def __init__(self):
    
    def add(self, a, b = None):
    
    def sub(self, a, b = None):
        
    def mul(self, a, b = None):
        
    def div(self, a, b = None):
    
```

How to use:

```python
calc = Calculator()
    
    print("Addition with two arguments (2 + 3):", calc.add(2, 3))
    print("Addition with one argument (adding 2 to memory):", calc.add(2))
    
    print("Subtraction with two arguments (5 - 3):", calc.sub(5, 3))
    print("Subtraction with one argument (subtracting 5 from memory):", calc.sub(5))
    
    print("Multiplication with two arguments (2 * 3):", calc.mul(2, 3))
    print("Multiplication with one argument (multiplying memory by 2):", calc.mul(2))
    
    print("Division with two arguments (6 / 3):", calc.div(6, 3))
    print("Division with one argument (dividing memory by 6):", calc.div(6))
```
