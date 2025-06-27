
#insertion
f=-1
r=-1
q=[]
n=5
 
if f==(r+1)%n:
    print("queue full ")             # first check queue if full 
if f==-1 and r==-1:                  # if queue is not full and queue is having more elements 
    f=(f+1)%n 
    r=(r+1)%n
    a=int(input())
    q[r] = 0 
else:
    r=(r+1)%n                         # if first false and second oine is false then r = 0.1.2.3.4.0.1.2.3.
    a=int(input())
    q[r] = a        

#deletion:
f=-1
r=-1
q=[]
n=5

if f==-1 and r==-1: 
    print("empty")

elif f==r:
    x=q[f]
    f=-1                      #empty 
    r=-1
    print (x)    #in print write return   
else:
    x=q[f] 
    f=(f+1)%n
    print (x)    #in print write return   


#printing data:
f=-1
r=-1
q=[]
n=5

if f==-1 and r==-1: 
    print("no data")

elif f<r:
    for i in range(f,r+1,1):
        print(q[i])

else:            #f>r
    for i in range(f,n,1):
        print(q[i])
    for i in range(0,r+1,1):
        print(q[i])
