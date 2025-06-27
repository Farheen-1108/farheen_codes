e,n,w,s = map(int,input().split())
x = e-w
y = n-s
if (x>0 and y>0):
    print("north east")
if (x<0 and y>0):
    print("north west")
if (x<0 and y<0):
    print("south west")
if (x>0 and y <0):
    print("south east")
if (x==0 and y!=0):
    print("north")
if (x!=0 and y==0):
    print("east")
if (x<0 and y==0):
    print("west")
if (x==0 and y!=0):
    print("south")
