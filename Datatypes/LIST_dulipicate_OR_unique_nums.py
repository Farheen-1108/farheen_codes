size=int(input("name of elements: "))
list=[]
unique_list=[]
for i in range(size):
    temp = int(input(f"enter the integer value in {i} position"))
    list.append(temp)
print("user entered list:",list)
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print("unique list : ",unique_list)