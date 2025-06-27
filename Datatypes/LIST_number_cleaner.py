num = int(input("enter the value of numbers: "))
list=[]
for i in range(num):
    temp = int(input(f"enter the integer value {i} index position : "))
    list.append(temp)
print("user entered list ",list)
for i in range(num):
    if (list[i]<0):
        list[i]=0
for i in range(num):
    if(list[i]%3==0):
        print(list[i])
print("updated list ",list)
