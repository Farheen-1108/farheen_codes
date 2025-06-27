size = int(input("enter the size of list: "))
list=[]
for i in range(size):
    temp = int(input(f"enter the integer value {i} index position : "))
    list.append(temp)
print("user entered list ",list)