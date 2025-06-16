size = input("enter the size of list: ")
list=[]
for i in range(10):
    temp = input(f"enter the songs {i} index position :")
    list.append(temp)
print("songs list : ",list)
print("reversing the list:")
print(list[::-1])