num = int(input("enter the number of value: "))
e_list = []
o_list = []
for i in range (1,num+1,2):
    o_list.append(i)
for i in range (2,num+1,2):
    e_list.append(i)
print("even list",e_list)
print("odd list",o_list)