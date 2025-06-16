ipl =["csk","rcb","mi","srh","gt","pbks"]
print("access without index loop: ")
for i in ipl:
    print(i)
print("access with index loop: ")
for i in range(len(ipl)):
    print(ipl[i])
print("while using while loop: ")
i=0
while(i<len(ipl)):
    print(ipl[i])
    i+=1
