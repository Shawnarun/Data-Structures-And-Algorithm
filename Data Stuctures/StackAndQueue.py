# Stack and Queue

queue=[]
stack =[]

#=======================================================
#Adding Element

queue.append(5) # Enqueue
stack.append(5) #Push

queue.append(14) # Enqueue
stack.append(14) #Push

#=======================================================

#Accessing Last Element
#queue = [ 5 , 14]
#stack = [5 , 14]
print("Last Element : ", queue[0])
print("Last Element : ", stack[-1])

#=======================================================
#Removing Element
#queue = [ 5 , 14]
#stack = [5 , 14]

queue.pop(0) #Dequeue
stack.pop()  #Pop

print("queue" ,queue)
print("stack" ,stack)

#=======================================================
#Check length
print(len(stack))
print(len(queue))

#=======================================================
#isEmpty
print(len(stack) == 0)
print(len(queue) == 0)