# insertion sort ex cards:

import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i] = a
print(x)

for i in range (1,n,1):
    data = x[i]
    j = i
    while(j>0 and x[j-1] > data):            #x[j-i] = small data
        x[j] = x[j-1]                      # changing the smallest index to backward # swapping line
        j-=1
    x[j] = data                             # swapping line
    print(x)
print(x)


#descending order:
import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i] = a
print(x)

for i in range (1,n,1):
    data = x[i]
    j = i
    while(j>0 and x[j-1] < data):            #x[j-i] = small data
        x[j] = x[j-1]                      # changing the smallest index to backward # swapping line
        j-=1
    x[j] = data                             # swapping line
    print(x)
print(x)
