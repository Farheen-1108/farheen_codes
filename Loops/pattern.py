num=int(input())
for rows in range(0,num+1):
    for cols in range(1,rows+1):
        print("*",end=" ")
    print()

num = int(input())
for i in range(1,num+1):
    for space in range(1,num-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

num = int(input())
for i in range(1,num+1):
    for space in range(1,i):
        print(" ",end=" ")
    for j in range(1,num-i+2):
        print("*",end=" ")
    print()

num = int(input())
sp = num-1
st = 1
for i in range(num):
    for space in range(sp):
        print(" ",end="")
    for j in range(st):
        print("*",end="")
    print()
    sp = sp-1
    st = st+2

num = int(input())
for i in range(num):
    for j in range(num):
        if i==0 or i==num-1 or j==0 or j==num-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


num = int(input())
for i in range(num+1):
    for j in range(num+1):
        if i==0 or j==0 or i==num or j==num:
            print("*",end="")
        else:
            print(" ",end="")
    print()

num = int(input())
for i in range(num):
    for space in range(num-i+1):
        print(" ",end="")
    for j in range(i+1):
        if i==num-1 or j==0 or j==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

num = int(input())
for i in range(1,num+1):
    for space in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        if i==num or j==1 or j==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

num = int(input())
for i in range(1,num+1):
    for space in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1 or j==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
for i in range(1,num+1):
    for space in range(1,i+1):
        print(" ",end="")
    for j in range(1,num-i+1):
        if j==num-i or j==1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

num = int(input())
for i in range(1,num+1):
    for space in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,i+1):
            print("* ",end="")
    print()
for i in range(1,num+1):
    for space in range(1,i+1):
        print(" ",end="")
    for j in range(1,num-i+1):
            print("* ",end="")
    print()
        
