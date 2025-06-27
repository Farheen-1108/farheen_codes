'''  stack is a data structure based on the principle LIFO 
list size is dynamic in python '''
st = []*4                # datastructure size is 4
st.append(10)            # it will store in index of 0
st.append(20)
st.append(30)
st.append(40)
st.append(50)            # we can add extra value with irrespective of size st=[]*4
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)                  # the stack is empty


from collections import deque              # deque class ki size ni specify chesidhi from collections
st=deque(maxlen=4)                         # len size = 4  (maxlen = parameter)
st.append(10)                              # no need to check condition in this stack
st.append(20)
st.append(30)
st.append(40)                # if give an extra value it will not print all it will delete first value and new data is added in last 
st.append(50)
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)


from queue import LifoQueue              # we can create stack by using this class and information also 
st=LifoQueue(maxsize=4)                 
print(st.qsize()) 
st.put('a')                             # put() function to push,elements
st.put('b')
st.put('c')
print("Full: ",st.full())
print("Size: ",st.qsize())
print("\nelements popped from the stack")
print(st.get())
print(st.get())
print(st.get())




