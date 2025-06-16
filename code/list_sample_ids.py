s_1 = input("enter the lab sampl id : ")
s_2=""
list = []
n = int(input("enter the number of id's u have to generate: "))
for i in range(n):
   s_2 = (f"LAB2025-0{s_1+1}")
   list.append(s_2)
   s_1 += 1
print(list)
