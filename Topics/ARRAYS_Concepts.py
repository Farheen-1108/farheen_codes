# NumPy stands for Numerical Python.
# creating numpy array
import numpy as np                        # alias: In Python alias are an alternate name for referring to the same thing. (as)
arr = np.array([1,2,3,4,5])               # array object in numpy is ndarray
print(arr)
print(type(arr))

#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
# and it will be converted into an ndarray.

'''
NumPy is a Python library used for working with arrays. has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely .
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.
'''

'''
types of arrayes :
0-D array : Scalars, are the elements in an array. Each value in an array is a 0-D array.
1-D array : An array that has 0-D arrays *(as its elements)* is called uni-dimensional or 1-D array.
2-D array : An array that has 1-D arrays as its elements is called a 2-D array. often used to represent matrix or 2nd order tensors matrix operations called numpy.mat
3-D array : An array that has 2-D arrays (matrices) as its elements is called 3-D array.often used to represent a 3rd order tensor.






'''
# 0-D array:
import numpy as np 
arr = np.array(45)                      # there is no dimensions 
print(arr)
# 1-D array:
import numpy as np
arr = np.array((1,2,3,4,5))             # insert the list or tuples as 0-D
print(arr)
# 2-D array:
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])       # 2-D array containing two arrays , Field elements must be 2- or 3-tuples.
print(arr)
# 3-D array:
import numpy as np                      # Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6.
arr = np.array([[[1,2,3],[4,5,6]],[[2,3,4],[5,6,7]]])  
print(arr)

# ndim attribute that returns an integer that tells us how many dimensions the array have.
import numpy as np
arr = np.array(42)
print(arr.ndim)

# An array can have any number of dimensions. When the array is created,
# you can define the number of dimensions by using the **ndmin** argument.



