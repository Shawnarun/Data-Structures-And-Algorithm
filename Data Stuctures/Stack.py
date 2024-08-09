
stack =[]

# 5 , "Boyj"
#Push

stack.append(5)
stack.append("Boyj")
stack.append(9.0)

print(stack)

#Pop
stack.pop()
print(stack)

#Check Top element
print(stack[-1])


#isEmpty
print(len(stack) == 0)

#Size
print(len(stack))