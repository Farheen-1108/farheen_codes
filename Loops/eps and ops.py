num = int(input())
eps,ops = 0,0
pos =0
while(num>0):
    digit = num%10
    if pos%2==0:
        print(digit,end=" ")
    else:
        print(digit,end=" ")
    num = num//10
    pos = pos+1
