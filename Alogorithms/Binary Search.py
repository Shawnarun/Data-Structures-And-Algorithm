def BinarySearch(array, l, r, num):
    if r >= l:
        mid = l + (r - l) // 2

        if array[mid] == num:
            return mid

        elif array[mid] < num:
            return BinarySearch(array, mid + 1, r, num)

        else:
            return BinarySearch(array, l, mid - 1, num)

    else:
        return -1


arr = [2, 4, 8, 10, 14, 16]
print(BinarySearch(arr, 0, len(arr) - 1, 10))
