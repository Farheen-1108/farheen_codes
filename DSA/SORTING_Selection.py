# same as bubble algorithm 
'''
per stage one time only we swap
we store the value where the smallest data came
after comapring the all data now the swap is done after one stage is completed not everytime
30 , 50 , 10 , 40 , 20
max same as bubble sort 
'''
import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i] = a
print(x)

for i in range(0,n-1,1):                  # outer loop should stop at 3
    min1 = i                              # i = 0 for first stage s   i=1,2,3,4
    for j in range(i+1,n):                # inner loop should stop at 4
        if x[min1] > x[j]:                # j is got the smal value now it is stored in min1
            min1 = j
    x[i],x[min1] = x[min1],x[i]           # swap cases total 6 # i tho start chestunam and min1 lo store chestunnam
    print(x)                              # stage by stage

print(x)                                  # x[min1] = j

#descending order:

import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i] = a
print(x)

for i in range(0,n-1,1):                  # outer loop should stop at 3
    min1 = i                              # i = 0 for first stage s   i=1,2,3,4
    for j in range(i+1,n):                # inner loop should stop at 4
        if x[min1] < x[j]:                # j is got the smal value now it is stored in min1
            min1 = j
    x[i],x[min1] = x[min1],x[i]           # swap cases total 6 # i tho start chestunam and min1 lo store chestunnam
    print(x)                              # stage by stage

print(x)                                  # x[min1] = j