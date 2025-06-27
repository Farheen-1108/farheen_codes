num = int(input())
ans = 1
while num!=0:
    digit = num%10
    ans = ans*digit
    num = num//10
print(ans)
