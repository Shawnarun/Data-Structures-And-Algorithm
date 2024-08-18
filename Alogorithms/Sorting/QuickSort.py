import random


def QuickSort(array):

    if len(array) < 1:
        return array

    pivot = random.choice(array)

    left=[i for i in array if i< pivot]
    middle = [i for i in array if i== pivot]
    right = [i for i in array if i > pivot]


    # left =[]
    #
    # for i in array:
    #     if i < pivot:
    #         left.append(i)
    #
    # middle =[]
    # for i in array:
    #     if i == pivot:
    #         middle.append(i)
    #
    # right = []
    # for i in array:
    #     if i > pivot:
    #         right.append(i)

    return QuickSort(left) + middle +QuickSort(right)


arr = [4, 2, 5, 8, 7]
print(QuickSort(arr))