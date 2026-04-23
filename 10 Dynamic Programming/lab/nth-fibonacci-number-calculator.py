"""
Build an Nth Fibonacci Number Calculator
"""


def fibonacci(n: int) -> int:
    if n < 0:
        return 0
    sequence = [0] * (n + 1)
    sequence[1] = 1
    for i in range(2, n + 1):
        sequence[i] = sequence[i - 1] + sequence[i - 2]
    return sequence[n]


if __name__ == "__main__":
    print(fibonacci(3))
    print(fibonacci(5))
    print(fibonacci(7))
    print(fibonacci(15))
    print(fibonacci(40))
