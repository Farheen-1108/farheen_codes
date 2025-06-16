num = int(input("enter the num of table: "))
i = 1
while(i<=10):
    if (num%i==0 or num%i!=0):
        print(num,'x',i,'=',num*i)
    i = i+1
#a=10
#for i in range(1,a+1)