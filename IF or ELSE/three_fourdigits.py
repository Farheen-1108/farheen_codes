num = int(input("enter a num:"))
if ((num>=100 and num<=999) or (num<=-100 and num>=-999)) :
    print("three digit")
elif ((num>=1000 and num<=9999) or (num<=-1000 and num>=-9999)):
    print("four digit")
else:
    print("not number")

#ternary operators
#result="three or four digit" if(num>=100 and num<=999 or num<=-100 and num>=-999)  elif(num>=1000 and num<=9999 or num<=-1000 and num>=-9999) else "number"
#print(f"{num} is {result}") 