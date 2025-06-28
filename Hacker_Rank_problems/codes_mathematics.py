# army game 
def gameWithCells(n, m):
    x = (n+1)//2
    y = (m+1)//2
    return x*y

#Diwali Lights
''' 2 power the n (on & off for yhe lights)
    for dice it is 6 power to n
    2 aa input then ans will be 4 
'''
def lights(n):
    np = (2**n)-1
    return np%pow(10,5)  #in this the(cause light have two statues one off) 2 pow is done with n and (-1)

#Minimum Height Triangle
''' area of triangle = 1/2 * b * h
we want greatest round figure so used the ceil from math import '''
'''
def lowestTriangle(trianglebase, area):
    h = (math.ceil((2*area)/trianglebase))
    return h
'''

#extra long factorial:
def extraLongFactorials(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
#or 
 #  print(math.factorial(n))      #direct math module


#flipping the bits
''' example
n = 14
1110
flipping the bits = 3
1001
2^3+2^2+2^1+2^0 == 1001  (2 to the power of 0 is equal to 1)
bit xor operation

N^(2**3)-1
14^7
1110
0111
-----
1001
bit wise xor   : same = 0 , different = 1
'''
def flippingBits(n):
    a = (n^(2**32)-1)
    return a
'''
number conversion: 6 types D -- B , B -- D , D -- O , O -- D , D -- H , H -- D.
binary(B)
decimal(D) = 2
octal(O) = 8
hexadecimal(H) = 16
for hecadecimal --              10,11,12,13,14
            0,1,2,3,4,5,6,7,8,9,a,b,c,d,e.
'''
#Drawing Book
def pageCount(n, p):
    fc = p//2
    bc = (n//2)-(p//2)
    return min(fc,bc)

# or 

def pageCount(n, p):
    fc = p//2
    bc = (n//2)-(p//2)
    if fc < bc :
        return fc
    else:
        return bc
    

#Cats and a Mouse
def catAndMouse(x, y, z):
    d1 = abs(x-z)
    d2 = abs(y-z)
    if (d1 == d2):
        return "Mouse C"
    elif (d1>d2):
        return "Cat B"
    else:
        return "Cat A"
    
