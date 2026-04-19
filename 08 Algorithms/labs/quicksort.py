"""
Implement the Quicksort Algorithm
"""


def quick_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    # result=[]
    number1 = [x for x in numbers if x < pivot]
    number2 = [x for x in numbers if x == pivot]
    number3 = [x for x in numbers if x > pivot]

    return quick_sort(number1) + number2 + quick_sort(number3)


quick_sort([20, 3, 14, 1, 5])
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
