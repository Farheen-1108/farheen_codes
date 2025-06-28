''' array  is package of numpy . the function is array 
array has two types : one dimension and multi type dimension.  
array data are stored in continuously , and the index is started from [0]. 
'''

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
import numpy as np
n = int(input())
a = np.ndarray(shape=(n),dtype=int)
for i in range (n):
    x = int(input())
    a[i] = x
print(a)
d = int(input())                    # d = 7
ans=np.searchsorted(a,d)            # what is the index position of the new data only known in this
print(ans)
print(a)

#sorting the array
import numpy as np
n = int(input())
a = np.ndarray(shape=(n),dtype=int)
for i in range (n):
    x = int(input())
    a[i] = x
print(a)
a.sort()
print("after sort",a)


#in 2d the rows and column size should maybe not same but for matrix rows and columns should be same 
# 2 dimension array:
import numpy as np
x = [[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x) 
print(a)
print(a.dtype)
print(a.shape) 
print(a.ndim)
print(a.size)

# removal of symbol
x = [[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x) 
print(a)
print(*a)                #symbol removal * is used


# using for loop to removal of extra bracket
import numpy as np
x = [[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x) 
for i in a:
    print(i)              

# the num of rows range is 3 and column is 3 
import numpy as np
x = [[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x) 
for i in range(3):
    for j in range(3):
        print(a[i][j],end=' ')             #one time one row completed 
    print()

import numpy as np
x = [[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x) 
for i in range(3):
    for j in range(3):                      #one time one row completed 
        print(a[i][j],(i,j),end=' ')        # to print sub index with rows and colums we use i,j
    print()

    
# 2d array data matrix 
import numpy as np
x = [[1,2,3],[4,5,6],[7,8,9]]            # we cannot conversion the 2d into matrix
a = np.array(x)
m=np.matrix(x) 
ans = a.flatten()
print(ans)

# to get in bracket and flatten 
import numpy as np
x = [[1,2,3],[4,5,6],[7,8,9]]            # we cannot conversion the 2d into matrix
a = np.array(x)                          # stored in one variable
m=np.matrix(x) 
ans = a.flatten()
print(ans)
ans1 = m.flatten()
print(ans1)

#reshape
import numpy as np
x = [[1,2,3],[4,5,6]]           
a = np.array(x)               # x data converted into array
m=np.matrix(x)                # x data converted into matrix 
a1 = a.reshape(3,2)           # it will reshape the shape of rows and columns
print(a1)                     # converted result is stored in variable a1
m1=m.reshape(3,2)
print(m1)


# addition , substraction,multiplication,division,modular division,floor divisin:
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[4,5,6],[1,2,3]])
x = np.array(a)
m = np.matrix(a)
a = a + 1                      # constant addition
print(a)
a = a - 1                      # constant substraction
print(a)                        
a = a* 2                       # constant multiplication
print(a)                      
a = a/2
print(a)
m = m/2
print(m)
a%=2
print(a)
m%=2
print(m)
a**=2                         #exponential can not be happe for mtrix
print(a)
a = a//2
print(a)
m = m // 2
print(m)

import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
m = np.matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')
print(a)
print(a.sum())
print(m.sum())            # array and matrix sum is same 
print(a.sum(axis=1))      # axis is row wise operation takes place (sum)
print(m.sum(axis=1))  
print(a.sum(axis=0))      # axis = 0 column wise sum
print(m.sum(axis=0))  
print(a.cumsum())                   # adding elemnet data one by oe every sum is different
print(m.cumsum()) 

print(a.max())
print(m.max())
print(a.max(axis=1))
print(m.max(axis=1))
print(a.max(axis=0))
print(m.max(axis=0))

print(a.min())
print(m.min())
print(a.min(axis=1))
print(m.min(axis=1))
print(a.min(axis=0))
print(m.min(axis=0))

print(len(a))             # lenght of row = 3
print(len(m))

# product function
print(a.prod())
print(m.prod())
print(a.prod(axis=1))
print(m.prod(axis=1))
print(a.prod(axis=0))
print(m.prod(axis=0))


#transpose (converting rows into columns))
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
m = np.matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')
print(a.T)
print(m.T)

print(a.transpose())
print(m.transpose())

print(a.trace())    # trace is a function that prints the addition diagonal data
print(m.trace())

import numpy as np
a = np.array([[1,1,1],[2,2,2],[3,3,3]])
m = np.matrix('1, 1, 1; 2, 2, 2; 3, 3, 3')
print(np.unique(a))
print(np.unique(m))

#determinants of matrix:
import numpy as np
a = np.array([[6,1,1],[4,-2,5],[2,8,7]])
m = np.matrix('6,1,1;4,-2,5;2,8,7')
ans=np.linalg.det(a)
print(ans)
ans1=np.linalg.det(m)
print(ans1)
ans2 = m.mean()
print(ans2)
ans3 = m.mean()
print(ans3)

#zeros 
import numpy as np
a = np.zeros((3,4),dtype=int)
print(a)
import numpy as np
a = np.ones((3,4),dtype=int)
print(a)

import numpy as np
a = np.ones((3,4))
print(a)

a = np.full((3,4),5)
print(a)

#sort operations:
import numpy as np
a = np.array([[1,2,3],[3,6,9],[4,8,12]])
m = np.matrix('2,4,6;3,6,9;4,8,12')
x=np.sort(a,axis=0)
y=np.sort (m,axis=0)
print(x)
print(y)

#descending order (complete , row,column wise)
#complete
import numpy as np
a = np.array([[1,2,3],[3,6,9],[4,8,12]])
m = np.matrix('2,4,6;3,6,9;4,8,12')
x=(np.sort(-a,axis=None))*-1
print(x)
y=(np.sort(-a,axis=None))*-1
print(y)

#row wise
import numpy as np
a = np.array([[1,2,3],[3,6,9],[4,8,12]])
m = np.matrix('2,4,6;3,6,9;4,8,12')
x=(np.sort(-a,axis=1))*-1
print(x)
y=(np.sort(-a,axis=1))*-1
print(y)

#column wise
import numpy as np
a = np.array([[1,2,3],[3,6,9],[4,8,12]])
m = np.matrix('2,4,6;3,6,9;4,8,12')
x=(np.sort(-a,axis=0))*-1
print(x)
y=(np.sort(-a,axis=0))*-1
print(y)



#matrix addition,substraction,multiplication by using and comparing two matrix:
#addition
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[4,5,6],[1,2,3]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('4,5,6;1,2,3')
ans = np.sum([a,b],axis=1)
print(ans)
ans1=np.sum([c,d],axis=1)
print(ans1)

#sub
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[4,5,6],[1,2,3]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('4,5,6;1,2,3')
ans = np.diff([a,b],axis=1)
print(ans)
ans1=np.diff([c,d],axis=1)
print(ans1)

#product
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,0],[0,1],[1,0]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('1,0;0,1;1,0')
ans1=a.dot(b)
print(ans1)
ans=c.dot(d)
print(ans)

#array multiplication when sizes are same
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[1,0,1],[0,1,0],[1,0,1]])
print(a*b)
a

#joins:
list1 =['boe','batch','of','2023']
str1 = '@#'
print(str1.join(list1))
