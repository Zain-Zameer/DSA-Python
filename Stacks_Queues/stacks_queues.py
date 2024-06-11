# Stacks in python 
# stack = ['Ali','Ahmed','Akbar']
# print(stack)
# stack.append('Kashan')
# print(stack)
# stack.pop()
# print(stack)

# Queues in python 
# queues = ['Ali','Ahmed','Akbar']
# print(queues)
# queues.append('Kashan')
# print(queues)
# queues.pop(0)
# print(queues)

from collections import deque 
queue = deque(['Ali','Ahmed','Akbar','Kashan'])
print(queue)
queue.append('Okasha')
print(queue)
queue.pop()
print(queue)