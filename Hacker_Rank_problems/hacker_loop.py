# loop
n = int(input())
for i in range(0,n):
    print(i*i)
    i = i + 1         #without increment also it will print
# or
n = int(input())
i = 0
while (n>i):            # while <=n-1: also can be 
    print(i * i)
    i = i + 1         # but in this u should give the increment

# multiplication tables :
n = int(input())
i = 1
while (i<=10):
    print(n,"x",i,"=",n*i)
    i = i + 1
# or 
n = int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    i = i + 1

# Connecting Towns
def connectingTowns(n, routes):
    np = 1
    for i in routes:
        np*=i
    return np%1234567
''' or
def connectingTowns(n, routes):
   np = math.prod(routes)          # directly with out using loops
  return np%1234567

#digit separation
n = 124
r = n%10         #124%10 = 12
n = n//10        #124//10 = 12
# same up to we get the 1,0 
# 
'''

#find the digit 
def findDigits(n):
    c = 0
    r= n
    while(n!=0):
        digit = n % 10
        if digit != 0 and r%digit == 0:
            c = c+1
        n = n //10
    return c


# sum of digits:
n = int(input("enter the number:"))
sum = 0
while (n!=0):
    digit = n%10
    sum = sum + digit
    n = n//10
print(sum)

# or
n = int(input("enter the number:"))       #if n is zero (0) before only the sum is added 
sum = 0
while (n!=0):
    digit = n%10
    sum = sum + digit
    print(sum)
    n = n//10

# sum of individual digits of the given positive integers number n till the result is of single digit number
n = int(input("enter the number:"))
sum = 0
while (n!=0):
    digit = n%10
    sum = sum + digit
    n = n//10
    if (n==0 and sum>9):
        n = sum
        sum = 0
print(sum)

#chocolate feast:

def chocolateFeast(n, c, m):
    nc = n//c
    wa = nc
    while wa >=m:
        nc+=wa//m
        wa = (wa//m) + (wa%m)
    return nc

#xif fino:
def isFibo(n):
    a = 0
    b = 1
    if n==0 or n==1:
        return "IsFibo"
    else:
        while True:
            c = a+b
            if c == n:
                return "IsFibo"
                break
            if c>n:
                return "IsNotFibo"
                break
            a = b
            b = c
    