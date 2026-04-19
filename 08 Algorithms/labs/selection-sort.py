"""
Selection sort is another popular sorting algorithm taught in most computer science courses.

This algorithm works by repeatedly finding the smallest element from the unsorted portion of the list and swapping it with the first unsorted element.
It begins by selecting the minimum value in the entire list and swapping it with the first element.
Then it moves to the second position, finds the smallest value in the remaining unsorted elements, and swaps it with the second element.
This process continues, moving through the list one element at a time, until the entire list is sorted.

Selection sort results in a quadratic time complexity in the best, average, and worst case scenarios.
The space complexity will be constant O(1) because the sorting is done in place and a constant amount of memory is being used regardless of the size of the list.
"""


def selection_sort(items):
    nb_items = len(items)
    for i in range(nb_items - 1):
        min_list = items[i]
        min_index = i
        for j in range(i, nb_items):
            if items[j] <= min_list:
                min_list = items[j]
                min_index = j
        if min_index != i:
            temp = items[i]
            items[i] = items[min_index]
            items[min_index] = temp
    return items
