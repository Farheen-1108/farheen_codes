def prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("num is prime")
    else:
        print("num is not prime")
num = int(input("enter the number: "))
prime(num)


def is_prime(nums):
    count=0
    if num>1:
        for i in range(2,nums//2+1):
            if(nums%i==0):
                count+=1
        if count==0:
            print("num is prime")
    else:
        print("num is not prime")

nums = int(input("enter the number:"))
is_prime(nums)