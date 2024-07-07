# Stack using list

stack = [1, 4, 5, 6]

print(stack[-1])  # Accessing

stack.append(68)  # insertion
print(stack[-1])

stack.pop()  # Deletion
print(stack[-1])



# Stack using deque
from collections import deque

stack = deque([1, 2, 4, 5, 6])
print(stack[-1])


from queue import Queue

q =Queue()
q.put(5)
a=q.get()
print(a)
print(q.empty())
