#program to count the uppercase alphabets ,lower case alphabets ,digits and special aymbols present in the given strings
# ex Vignan College Bt @ 2025
s = input("enter the string")
uc = 0
lc = 0
d = 0
spl_case = 0
for ch in s:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+=1
    elif ch.isnumeric():
        d+=1
    else:
        spl_case+=1
print(uc)
print(lc)
print(d)
print(spl_case)

# or 
s = input("enter the string")
uc = 0
lc = 0
d = 0
spl_case = 0
for i in s:
    if i>='A' and i<='Z':
        uc+=1
    elif i>='a' and i<='z':
        lc+=1
    elif i>='0' and i<='9':
        d+=1
    else:
        spl_case+=1
print(uc)
print(lc)
print(d)
print(spl_case)


# chr and ord:
'''
chr means when we give digit we will get charater as output
ord means when we give charater we will get output as number 
asci number number means 

A = 65    Z = 90
a = 97    z = 122

ord  48 = 1
     57 = 9
'''