num = int(input("enter num: "))
digit = 0
while num!=0:
    digit += 1
    num = num//10
print(digit)