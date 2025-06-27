# key is taken and compared to every index data 
'''
if there is duplicates then where the first index meet then that will be answer (index)
'''
#non recursion :

import numpy as np
n = int(input())                                  # 9 elements
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):                                # loop exceute n times
    a=int(input())
    x[i] = a
print(x)

key = int(input())                                  # data to search
flag = 0
for i in range (n):
    if key == x[i]:                                 # data matching takes place and in index i
        print(i)
        flag = 1                                    # data indentified  initial value of data = 0
        break
if(flag==0):                                       # data still 0 
    print("data not present")   

# recurssive :

def rls(x,i,key):
    if key == x[i]:                               # x[4] data = input data # data matching takes place and in index i
        return (i)
    if (len(x)-1 == i):
        return -1
    return rls(x,i+1,key)                         # 

import numpy as np
n = int(input())                                  # 9 elements
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):                                # loop exceute n times
    a=int(input())
    x[i] = a
print(x)
key = int(input())
ans = rls(x,0,key)
if(ans==-1):
    print("data not present")
else:
    print("data identified",ans)


# from backside (highest side onwards):

def rls(x,i,key):
    if key == x[i]:                               # x[4] data = input data # data matching takes place and in index i
        return (i)
    if (i==0):
        return -1
    return rls(x,i-1,key)                         # 

import numpy as np
n = int(input())                                  # 9 elements
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):                                # loop exceute n times
    a=int(input())
    x[i] = a
print(x)
key = int(input())
ans = rls(x,n-1,key)
if(ans==-1):
    print("data not present")
else:
    print("data identified",ans) 