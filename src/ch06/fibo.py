"""Demonstrate module statements being executed on first import."""

print("Initialise", __name__)


def fib(n: int) -> None:
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()
