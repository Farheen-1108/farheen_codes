# binay search is also called as two way search algorithm
'''
calculating the middle value
and check with the middle index data with key : if not equal 
check > or < the middle value 
middle_1
'''

# ascending order:
n = int(input())
x = list(map(int,input().split(' ',n-1)))          #list value read operation statement
print(x)
x.sort()
print(x)
key = int(input())
low = 0
high = n-1
flag = 0
while low<=high:
    print(low,high)
    mid = (low+high)//2
    if x[mid] == key:
        print(mid)
        flag = 1            #data identified
        break
    elif key > x[mid]:
        low = mid + 1
    else:
        high = mid - 1
if (flag==0):
    print("data not present")


# desencing order:

n = int(input())
x = list(map(int,input().split(' ',n-1)))          #list value read operation statement
print(x)
x.sort(reverse=True)
print(x)
key = int(input())
low = 0
high = n-1
flag = 0
while low<=high:
    print(low,high)
    mid = (low+high)//2
    if x[mid] == key:
        print(mid)
        flag = 1            #data identified
        break
    elif key > x[mid]:
        high = mid - 1
    else:
        low = mid + 1
if (flag==0):
    print("data not present")


# recurssion:
def rbs(x,l,h,key):
    if l<=h:
        print(l,h)
        mid=(l+h)//2
        if x[mid]==key:
            return mid
        elif key>x[mid]:
            return rbs(x,mid+1,h,key)
        else:
            rbs(x,l,mid-1,key)
    return -1

n = int(input())
x = list(map(int,input().split(' ',n-1)))          #list value read operation statement
print(x)
x.sort(reverse=True)
print(x)
key = int(input())
low = 0
high = n-1
ans=rbs(x,low,high,key)
if ans==-1:
    print('data not found')
else:
    print(ans)