num1 = int(input("num1: "))
num2 = int(input("num2: "))
print("before swap:",num1,num2)
temp =0
temp = num1 + num2
num1 = temp - num1
num2 = temp - num1
print("after swap",num1,num2)