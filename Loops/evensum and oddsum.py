num = int(input())
es,os=0,0
while num>0:
    r=num%10
    if r%2==0:
        es+=r
    else:
        os = os+r
    num = num//10
print(abs(es-os))
