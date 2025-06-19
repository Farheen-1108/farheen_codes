''' array  is package of numpy . the function is array 
array has two types : one dimension and multi type dimension.  
array data are stored in continuously , and the index is started from [0]. '''

import numpy as np
x = np.array([10,20,30,40])
print(x)
print(type(x))
x = np.array([1.1,2.2,3.3])
x = np.array([2.2,"abc","ABC","def"])
x = np.array([1.1,2.2,3.3])

#constant addition,substraction,multiplication,division,modular divison and exponential

import numpy as np
x = np.array([1,2,3,4,5])
print(x)
x+=2        # x/=2 , x*=2 , x%=2 , x = x**2 , 
print(x)

# addition , substraction,multiplication , division,modules, moduledivision,floor division:

import numpy
a = numpy.array([1,2,3,4,5])
b = numpy.array([2,4,6,8,10])
c = a+b                                 
# a-b , a*b , a/b , a%b , a**b
print(c)

# sum() , max() , min(),len() function():
a = numpy.array([1,2,3,4,5])
print(sum(a))
a = numpy.array([1,2.2,3,4,5])
print(sum(a))

a = numpy.array([1,2,3,4,5])
print(max(a))

a = numpy.array([1,2,3,4,5])
print(min(a))
a = numpy.array([1,2,3,4,5,"abc"])
print(min(a))

#accessing of array in numpy is same as list data
import numpy
a = numpy.array([1,2,3,4,5,"abc"])
print(a)
print(*a)                        #comma removing method symbol removing

a = numpy.array([1,2,3,4,5,"abc"])
for i in a:
    print(i)
for i in range(len(a)):            # using index
    print(a[i])

a = numpy.array([1,2,3,4,5,"abc"])
print(a[::-1])                           # slicling 


# zero()-function:
# zeros(size,default)            # datatype is not a mandatory if we dont write it will print as real 
import numpy as np
a = np.zeros(5)
print(a)

# ones function
a = np.ones(4)                   # i. i. i. because we are not prepared data type
print(a)

a = np.ones(5,int)                 # 1. 1.,. 1. here we are data type
print(a)

a = np.array([1,2,3,4,5])
print(a.dtype)

a = np.array([1,2,3,4,5,"abc"])
print(a.dtype)
print(a.ndim)                         # ndim = dimensions of array
print(a.size)
a = np.array([1,2,3],[3,2,1])
print(a.shape)

# one dimension array :
import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range (n):
    v = int(input())
    x[i] = v
print(x)



# take an array with value 10,20,15,25,30 
# even index odd index
# program to print the index of the even , odd values present in the list:

import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range (n):
    v = int(input())
    x[i] = v
print(x)
ans=np.where(x%2==0)
print(ans)

import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range (n):
    v = int(input())
    x[i] = v
print(x)
ans=np.where(x%2!=0)
print(ans) 


# program to print the index of the given partiular value present in the list:
import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range (n):
    v = int(input())
    x[i] = v
print(x)
ans=np.where(x%2!=0)
print(ans)

import numpy as np
n = int(input())
x = np.ndarray(shape=(n),dtype=int)
for i in range (n):
    v = int(input())
    x[i] = v
print(x)
ans=np.where(x)
print(ans)

#find the index to insert new into the list in the correct position by maintaining the order
