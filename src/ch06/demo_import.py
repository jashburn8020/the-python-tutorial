"""Import a module to show statements and functions definitions being executed."""

import fibo

print("Initialise demo_import")

fibo.fib(5)

if __name__ == "__main__":
    import sys

    fibo.fib(int(sys.argv[1]))
