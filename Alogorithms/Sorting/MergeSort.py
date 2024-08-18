def MergeSort(arr):

  if 1 < len(arr):
    #Split array
    #[2,4,8] [6,9,10]
    mid= len(arr)//2
    leftArray = arr[:mid]
    rightArray = arr[mid:]

    # la =[2,4,8] ra=[6,9,10]
    # la [2 ,4] ra [8]   la [6 ,9] ra [10]
    #la [2 ] ra [4] ra [8]  la [6] ra [9] [10]

    MergeSort(leftArray)
    MergeSort(rightArray)

    lp=0
    rp=0
    fp=0

    while lp < len(leftArray) and rp < len(rightArray):
        if leftArray[lp] < rightArray[rp]:
            arr[fp]=leftArray[lp]
            lp+=1
        else:
            arr[fp] = rightArray[rp]
            rp += 1

        fp += 1

    while lp < len(leftArray):
        arr[fp]=leftArray[lp]
        lp+=1
        fp+=1

    while rp < len(rightArray):
        arr[fp] = rightArray[rp]
        rp += 1
        fp += 1

    return arr


arr = [4, 2, 5, 8, 7 , 58 , 96 , 1 , 1 ,45]
print(MergeSort(arr))






