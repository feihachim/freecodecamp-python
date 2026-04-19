"""
Implement the Quicksort Algorithm
"""


def quick_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    smaller, equal, larger = [], [], []
    for number in numbers:
        if number < pivot:
            smaller.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            larger.append(number)

    return quick_sort(smaller) + equal + quick_sort(larger)


list1 = [20, 3, 14, 1, 5]
list2 = [87, 11, 23, 18, 18, 23, 11, 56, 87, 56]
print(quick_sort(list1))
print(quick_sort(list2))
