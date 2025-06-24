#implementation by list :
''' contains methods like append and pop '''
stack = []
stack.append("welcome")
stack.append("to")
stack.append("class")
print(stack)
print(stack.pop())
print(stack)

#implementation by deque:

from collections import deque 
stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

#implementation by queue(lifo):

from queue import LifoQueue
stack = LifoQueue(maxsize=4)
stack.put(50)
stack.put(40)
stack.put(60)
stack.put(70)
print(stack.full())
print(stack.qsize())
print(stack.get())
print(stack)
print(stack.get())
print(stack.full())
