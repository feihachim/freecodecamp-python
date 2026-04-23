"""
Build an Nth Fibonacci Number Calculator
"""


def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    sequence = [0, 1]
    for i in range(2, n + 1):
        fibn = sequence[i - 1] + sequence[i - 2]
        sequence.append(fibn)
    return sequence[n]
