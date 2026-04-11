"""
In this lab you will practice the basics of Python by building a small app that creates a number pattern.
"""


def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    result = ""
    for i in range(1, n):
        result += str(i) + " "
    result += str(n)
    return result
