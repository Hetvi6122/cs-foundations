"""
Author: Hetvi Patel
Description: Simple recursion examples for CS Foundations.
"""

def factorial(n):
    """Return factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    """Return nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print("Factorial(5):", factorial(5))
    print("Fibonacci(7):", fibonacci(7))
