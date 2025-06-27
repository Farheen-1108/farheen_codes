#SORTING:
# BUBBLE SORT
'''
comparision of an element  with the remaining next elements one by one.
if the first element is less than the second element no change.
if the first element is greater than the second element then performing swapping opertion 
to arrange in ascending order.
30 , 50 , 10 , 40 , 20
swap = a,b=b,a     x[i]>x[j] == swap      everytime
'''
#ascending order:
import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i] = a
print(x)

for i in range(0,n-1,1):                    # outer loop should stop at 3
    for j in range(i+1,n):                  # inner loop should stop at 4
        if x[i]>x[j]:
            x[i],x[j] = x[j],x[i]
            print(x)                        # swap cases total 6
print(x)

#descending order:
import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i] = a
print(x)

for i in range(0,n-1,1):                    # outer loop should stop at 3
    for j in range(i+1,n):                  # inner loop should stop at 4
        if x[i]<x[j]:
            x[i],x[j] = x[j],x[i]
            print(x)                        # swap cases total 6
print(x)