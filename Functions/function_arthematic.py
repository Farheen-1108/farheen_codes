#without return
def arthematic(x,y):
    c = x+y
    d = x-y
    e = x * y
    f = x / y
    g = x // y
    h = x % y
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
arthematic(2,3)

#with return
def arthematic(x,y):
    c = x+y
    d = x-y
    e = x * y
    f = x / y
    g = x // y
    h = x % y
    return(c,d,e,f,g,h)
res = arthematic(2,3)
print(res)    