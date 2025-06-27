s = input("enter the input values: ")
A = 0
C = 0
T = 0
G = 0
for i in s:
    if i == 'A':
        A+=1
    elif i =="C":
        C+=1
    elif i == "T":
        T+=1
    else:
        G+=1
#print("{"+" A :" +str(A)+" C :" +str(C)+" T :" +str(T)+" G :" +str(G)+"}")

dict = {"A":A, "C":C, "T":T,"G":G}
print(dict)