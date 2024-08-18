arr = [4, 2, 5, 8, 7]
x=81

for i in range(0, len(arr)):
    if arr[i] == x:
        print("your element present at : ",i)
        break
else:
    print(x," is not present in array")