q = []*4        # this is not a accurate info beacuse the size is not fixed
q.append(10)
print(q)
q.append(20)
print(q)
q.append(30)
print(q)
q.append(40)
print(q)
q.append(50)
print(q)
i=0
q.pop(i)
print(q)
i=0
q.pop(i)
print(q)
i=0
q.pop(i)
print(q)
i=0
q.pop(i)
print(q)


#implementation of deque:
from collections import deque
lq = deque(maxlen=4)
lq.append(10)
print(lq)
lq.append(20)
print(lq)
lq.append(30)
print(lq)
lq.append(40)
print(lq)
lq.append(50)               # first it will print 10,20,30,40 but if add extra value then it will delete first value(10)
print(lq)
lq.popleft()                 # first 10 delete
print(lq)
lq.popleft()
print(lq)
lq.popleft()
print(lq)
lq.popleft()
print(lq)