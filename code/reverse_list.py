size = int(input("enter the size of list: "))
list=[]
rev = 0
for i in range(size):
    temp = int(input(f"enter the integer value {i} index position : "))
    list.append(temp)
print(list[::-1])

