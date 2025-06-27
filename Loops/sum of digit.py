num = int(input())
ans = 0
while num!=0:
    digit = num%10
    ans += digit
    num = num//10
print(ans)
