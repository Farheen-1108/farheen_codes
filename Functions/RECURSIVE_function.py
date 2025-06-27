'''
a function calling itself is called recursive function.
function calling again itself 
advantages :
complex problem is solved easily with help of recursion , reusability .

*** The programs written by using loops is called non-recursion 
using functions is call recursion ***

adding of data and deleting of data is principle 

stack data structure :
last in first out (LIFO) ex : cd box , caller dial , 
'''
# write a recursive program to print the number srom A to B , where A = low value and B = high value:
# ex: A = 5 B = 10 OUTPUT : 5,6,7,8,9,10
#non recursive:

n1 = int(input())
n2 = int(input())
for i in range (n1,n2+1):
    print(i)
#or 
while(n1<=n2):
    print(n1)
    n1+=1

#recursion:
def rlh(x,y):                      #rucursion low to high (rlh)
    if(x<=y):
        print(x)
        x+=1
        rlh(x,y)                   #recursive calling statement (memory allocated more)
a,b = map(int,input().split())     #calling function
rlh (a,b)

# same function calling is written in both the def and calling than it is recursive statement
# if it ius deiffen then it is nested recursive 

# write program print A to B high valu to low value 
def rlh(x,y):
    if(x>=y):
        print(x)
        x-=1
        rlh(x,y)
a,b = map(int,input().split())
rlh (a,b)

# write a program to print the fact of the number by using recurssion
def rlh(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
n = int(input())
rlh(n)
# non recusive while loop:
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)      #recursive calling
n = int(input())                #calling function
f=fact(n)
print(f)
#non-recursive:
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
#while:
while(n>=1):
    f*=n
    n-=1
print(f)

def fact(n,a,b):
    if (n==0 or n==1):
        print(n)
    if(n==a):
        print(b)
    else:
        n-=1
        return fact(n,a,b*n)
n = int(input())
f = fact(n,1,n)
'''
 lcm(a,b) = (a*b)/gcd(a,b)
 gcd (a,b) = (a*b)/lcm(a,b)  
'''
#write to find the gcd of given numbers:
import math
print(math.gcd(5,12))
print(math.lcm(5,12))

#gcd using non recurssion:
a,b = map(int,input().split())
while a!=b:
    print(a,b)
    if a>b:
        a = a-b
    else:
        b = b-a
print(a)
print(b)

#recursive method:
def rgcd(a,b):
    if(a==b):
        return a
    if (a>b):
        return rgcd(a-b,b)
    else:
        return rgcd(a,b-a)
    
a,b = map(int,input().split())
ans = rgcd(a,b)
print(ans)

#recursion lcm:
def rlcm(a,b,x,y):
    if(a==b):
        return (x*y)//a
    if (a>b):
        return rlcm(a-b,b,x,y)
    else:
        return rlcm(a,b-a,x,y)
    
a,b = map(int,input().split())
ans = rlcm(a,b,a,b)
print(ans)

#feature of python instead of c:
import sys
sys.setrecursionlimit(100)   #function for the recursion function
def vignan():
    global i              #change the function i = 0 to i =1 by using global function
    i+=1
    print(i)
    vignan()               # recursive call
i = 0
vignan() #calling function

# tower of  hanoi:
def toh(n,a,b,c):                 # a = input , b = temp , c = output
    if(n>0):
        toh(n-1,a,c,b)
        print(a,'->',c)
        toh(n-1,b,c,a)
n = int(input())
toh(n,'a','b','c')









