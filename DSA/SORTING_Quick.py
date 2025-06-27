# quick sort also divide and conquer
'''
take any one elemnet and divide the list in two parts (element is call pivot element)
pivot as first , last  or median(pivot) any thing can be taken
taking middle value as pivot and dividing the elemnets two based on pivot small and bigger the 
element is smaller than pivot is left side and bigger is right
fast technic amd huge input data (more data)
'''

# ascendind order:
def qs(arr):
    global a
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]               # len = 5
    print(pivot,a)
    a+=1
    left = [i for i in arr if i<pivot]     # list comprehension (expression(3), loop(1) and condition(2))
    middle = [i for i in arr if i==pivot]   
    right = [i for i in arr if i>pivot]
    return qs(left) + middle + qs(right)   # recurssive call (2 for right and left)

a = 1
n = int(input())
x = list(map(int,input().split(' ',n-1)))        #split input in single line
print(x)
ans = qs(x)                 #calling function
print(ans)

# descending order

def qs(arr):
    global a
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]               # len = 5
    print(pivot,a)
    a+=1
    left = [i for i in arr if i<pivot]     # list comprehension (expression(3), loop(1) and condition(2))
    middle = [i for i in arr if i==pivot]   
    right = [i for i in arr if i>pivot]
    return qs(right) + middle + qs(left)   # recurssive call (2 for right and left)

a = 1
n = int(input())
x = list(map(int,input().split(' ',n-1)))        #split input in single line
print(x)
ans = qs(x)                 #calling function
print(ans)