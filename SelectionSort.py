arr = [4, 2, 5, 8, 7]

for i in range(len(arr) - 1):
    minIndex = i
    for k in range(i + 1, len(arr)):
        if arr[minIndex] > arr[k]:
            minIndex = k
    arr[minIndex],arr[i]=arr[i],arr[minIndex]

print(arr)
