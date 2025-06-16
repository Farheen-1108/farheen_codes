A=input("enter the name: ")
B=int(input("enter a number: "))
C=input("enter a mail: ")
r=""
for i in range (len(A)):
    if A[i].isalpha():
        r+=A[i]
if r.isalpha():
    print("valid name")
else:
    print("Invalid name")
B=str(B)
u=""
for i in range(len(B)):
        if B[i].isdigit():
            u=B[i]
if u.isdigit() and len(B)==10:
    print("Valid number")
else:
    print("Invalid number") 
n_c=0
a_c=0
s_c=0
length=len(C)
for i in range(length):
    char=C[i]
    if char.isdigit():
        n_c+=1
    elif char.isalpha():
        a_c+=1
    else:
        s_c+=1
if n_c>=1 and a_c>=1 and s_c>=1:
    print("Valid passward")
else:
    print("In valid passward")