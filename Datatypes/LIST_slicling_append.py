num = int(input("enter the elements: "))
list=[]
for i in range(num):
    str = input()
    list.append(str)
    l=list[:] + list[-3:]
print(l)
