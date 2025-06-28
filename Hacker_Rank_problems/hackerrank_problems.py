''' halloean sale:
s = 70  p=20 d = 3 m =6  cg=1
s = 50  p =17    cg= 2
33      14         3
19      11        4
8       8          5
'''
def howManyGames(p, d, m, s):
    cg = 0
    while(s>=p):
        s=s-p
        p = p-d
        cg+=1
        if p<m:
            p=m
    return cg

#factors:
n = int(input())
fact = 1
while(fact<=n):
    if (n%fact==0):
        print(fact)
    fact = fact+1
# or
n = int(input())
ff=1
lf = n
print(ff)
for i in range(2,(n//2)+1,1):
    if n%i==0:
        print(i)
print(lf)

#Sherlock and Divisors:
def divisors(n):
    i=1
    c = 0
    while i*i<=n:
        if(n%i==0):
            if(i%2==0):
                c+=1
        if i*i!=n:
            if(n/i)%2==0:
                c+=1
        i+=1
    return c

#sum vs xor:
def sumXor(n):
    c=1
    while n>0:
        if n%2==0:
            c*=2
        n = n//2
    return c

#sum of array :
n = int(input("enter the numbers:"))
arr = []
tsum = 0
for i in arr:
    tsum+=i
print(tsum)
#or
def simpleArraySum(ar):
    return sum(ar)


#Plus Minus
def plusMinus(arr):
    x = len(arr)
    pc,nc,z=0,0,0
    for i in arr:
        if i>0:
            pc+=1
        elif i<0:
            nc+=1
        else:
            z+=1
    print('%.6f'%(pc/x))
    print('%.6f'%(nc/x))
    print('%.6f'%(z/x))

#Compare the Triplets
def compareTriplets(a, b):
    fc,sc=0,0
    for i in range(3):
        if(a[i]>b[i]):
            fc+=1
        if(a[i]<b[i]):
            sc+=1
    return fc,sc

