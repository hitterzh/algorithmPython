

def selection_sort(arr):
    lengeth = len(arr)
    if lengeth < 2:
        return arr

    for i in range(lengeth - 1):
        least = i

        for j in range(i+1, lengeth):
            if arr[j] < arr[least]:
                least = j

        if least != i:
            arr[i], arr[least] = arr[least], arr[i]

    return arr

def bubble_sort(arr):

    length = len(arr)
    if length < 2:
        return arr

    for i in range(length -1, 0, -1):

        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


    return arr


def insertion_sort(arr):

    length = len(arr)
    if length < 2:
        return arr

    for i in range(1, length):

        for j in range(i, 0, -1):

            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr

def my_shell_sort(arr):
    length = len(arr)
    if length < 2:
        return arr

    gap = int(length / 2)

    while gap > 0:

        for i in range(gap, length):
            j = i

            while j > gap and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap

        gap = int(gap/2)

    return arr

def shell_sort(collection):
    """Pure implementation of shell sort algorithm in Python
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending
    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        for i in range(gap, len(collection)):
            j = i
            while j >= gap and collection[j] < collection[j - gap]:
                collection[j], collection[j - gap] = collection[j - gap], collection[j]
                j -= gap
    return collection


