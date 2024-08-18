
def BinarySearch(array,l,r,num):
    if r >= l:
        mid = l + (r -l) // 2
        if array[mid] == num:
            return mid

        elif array[mid] < num:
            return BinarySearch(array,mid+1,r,num)

        elif array[mid] > num:
            return  BinarySearch(array,l,mid-1,num)

    else :
        print(num," is not present in array")


arr = [4, 2, 5, 8, 7]
print(BinarySearch(arr,0,len(arr)-1, 81))