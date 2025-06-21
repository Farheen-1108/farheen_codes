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

def lowestTriangle(trianglebase, area):
    h = (math.ceil((2*area)/trianglebase))
    return h

#extra long factorial:
def extraLongFactorials(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
#or 
   print(math.factorial(n))      #direct math module


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
    
#Library Fine+
def libraryFine(d1, m1, y1, d2, m2, y2):
    if (y1<y2):
        return 0
    if y1!=y2:
        return 10000
    else:
        if m1<m2:
            return 0
        if m1!=m2:
            return 500 * abs(m1-m2)
        else:
            if d1<d2:
                return 0
            else:
                return 15*abs(d1-d2)          
#Taum and B'day
def taumBday(b, w, bc, wc, z):
    if (abs(bc-wc)<=z):
        return b * bc + w * wc
    elif bc>wc:
        return w*wc + (wc+z)*b
    else:
        return b*bc + (bc+z)*w
