
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("factorial only accepts integers")
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
