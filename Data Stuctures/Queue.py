# using list

queue = []


#Enqueue //
queue.append(5)
queue.append("Shawn")
queue.append(2.0)

print(queue[0])
print(queue[1])
print(queue[2])

#length
print(len(queue))

#Empty or Not
print(len(queue) == 0)


#Dequeue
queue.pop(0)
queue.pop(0)
queue.pop(0)

#Empty or Not
print(len(queue) == 0)


print(queue)

