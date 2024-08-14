arr =[4 , 2 , 6 , 8 , 1 , 12]

for i in range(1 , len(arr)):
    sortElement= arr[i]
    rightPointer = i-1

    while rightPointer >=0 and arr[rightPointer] > sortElement:
        arr[rightPointer+1] = arr[rightPointer]
        rightPointer -=1


    arr[rightPointer +1] = sortElement


print(arr)