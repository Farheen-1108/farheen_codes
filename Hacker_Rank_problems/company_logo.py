n = int(input())
base = 1
r = 0
d =0
while(n>0):
    d = n%10
    n = n//2
    r = r%10 + d
    base = base*2
print(base)
