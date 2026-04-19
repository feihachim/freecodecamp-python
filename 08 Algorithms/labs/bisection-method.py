"""
The bisection method, also known as the binary search method, uses a binary search to find the roots of a real-valued function.
It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

For example, if the tolerance is 0.01, the bisection method will keep halving the interval until the difference between the upper and lower bounds is less than or equal to 0.01.

In this lab, you will implement a function that uses the bisection method to find the square root of a number.
"""


def square_root_bisection(
    square_target: float, tolerance: float = 1, max_iterations: int = 5
):
    if square_target < 0:
        # Square root of negative number is not defined in real numbers
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )
    if square_target == 1 or square_target == 0:
        root = 1
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    # Ensures the interval covers the root for N < 1 and N > 1
    high = max(1, square_target)
    root = None
    i = 0
    while i < max_iterations and root is None:
        mid = (low + high) / 2
        square_mid = mid**2

        if abs(high - low) < tolerance:
            root = mid

        elif square_mid < square_target:
            low = mid
        else:
            high = mid
        i += 1

    if i == max_iterations:
        print(f"Failed to converge within {max_iterations} iterations")
    else:
        print(f"The square root of {square_target} is approximately {root}")
    return root


square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(225, 1e-7, 10)
