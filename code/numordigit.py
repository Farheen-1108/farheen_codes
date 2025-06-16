num = int(input("enter a num:"))
if (num>=10 and num<=99 or num<=-10 and num>=-99):
    print("two digit")
else:
    print("number")

#ternary operators
result="two digit" if(num>=10 and num<=99 or num<=-10 and num>=-99) else "number"
print(f"{num} is {result}")