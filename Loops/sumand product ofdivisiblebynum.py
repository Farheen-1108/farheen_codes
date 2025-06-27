a,b = map(int,input().split())
x = int(input())
s,p=0,1
while a<=b:
    if a%x==0:
        s = s+a
        p = p*a
    a=a+1
print(s)
print(p)
print(abs(s-p))
