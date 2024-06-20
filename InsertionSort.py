arr = [4, 2, 5, 8, 7]

for i in range(1, len(arr)):
    curVariable = arr[i]
    sortedArrayLastIndex = i - 1

    while sortedArrayLastIndex >=0 and curVariable< arr[sortedArrayLastIndex]:
        arr[sortedArrayLastIndex +1] = arr[sortedArrayLastIndex]
        sortedArrayLastIndex-=1

    arr[sortedArrayLastIndex+1] = curVariable
print(arr)
