num = int(input("enter the value of num: "))
# if -else
if num>0:
    print(f"{num} is +ve number")
elif num<0:
    print(num,"is -ve number")
else:
    print("zero")

#ternary operators:
result="+ve number" if(num>0) else "-ve number"
print(f"{num} is {result}")