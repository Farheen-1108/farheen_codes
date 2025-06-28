# binary to decimal and decimal to binary conversion 
n = int(input("enter the number:"))
x = bin(n)
print(x)
print(type(x))
print(x)
'''x = x[2:]
print(x)'''
de = int(x,2)                 # data to convert(x) , base of data(2)
print(de)


# octal to decimal and decimal to octal conversion 
n = int(input("enter the number:"))
x = oct(n)
print(x)
print(type(x))
print(x)
'''x = x[2:]
print(x)'''
de = int(x,8)                 # data to convert(x) , base of data(2)
print(de)

# hexadecimal to decimal and decimal to hexadecimal conversion 
