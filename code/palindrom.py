num = int(input("enter the num: "))
r = 0
temp = num
while(num!=0):
    digit = num%10
    r = r*10+digit
    num = num//10
if r == temp:
    print("is palindrome")
else:
    print("not palindrome")
