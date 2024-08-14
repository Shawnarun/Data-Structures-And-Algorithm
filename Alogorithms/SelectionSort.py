arr =[4 , 2 , 6 , 8 , 1 , 12]

for i in range(len(arr)-1):
    minIndex = i
    for k in range(i+1,len(arr)):
        if arr[minIndex] > arr[k]:
            minIndex=k

        # temp= arr[minIndex]
        # arr[minIndex] = arr[i]
        # arr[i]=temp
    arr[minIndex],arr[i]= arr[i],arr[minIndex]


print(arr)