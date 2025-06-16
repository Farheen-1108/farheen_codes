str1 = input("enter the first sequence: ")
str2 = input("enter the second sequence: ")  
print("str1",str1)
print("str1",str2)
if len(str1) != len(str2):
    print("error , print the same lenght")
list = []
for i in range(len(str1)):
    if str1[i] != str2[i]:
        list.append(i)
print(list)