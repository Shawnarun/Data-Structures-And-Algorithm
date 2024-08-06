def MergeSort(array):
    #split array
    if 1 < len(array):
        mid = len(array) // 2
        leftArray = array[:mid]
        rightArray = array[mid:]

        MergeSort(leftArray)
        MergeSort(rightArray)

        lp = 0
        rp = 0
        fp = 0

        while lp < len(leftArray) and rp < len(rightArray):
            if leftArray[lp] < rightArray[rp]:
                array[fp] = leftArray[lp]
                lp += 1
            else:
                array[fp] = rightArray[rp]
                rp += 1
            fp += 1

        while lp < len(leftArray):
            array[fp] = leftArray[lp]
            lp += 1
            fp += 1

        while rp < len(rightArray):
            array[fp] = rightArray[rp]
            rp += 1
            fp += 1

    return array


arr = [4, 2, 5, 8, 7]
print(MergeSort(arr))
