a = int(input())
b = int(input())
ans = 0
while a<=b:
    if (a%5==0 and a%3==0):
        ans = ans+a
    a = a+1
print(ans)
