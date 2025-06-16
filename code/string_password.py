A=input()
n_c=0
a_c=0
s_c=0
length=len(A)
for i in range(length):
    char=A[i]
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