#descending pripority

class pq:
    def __init__(self):
        self.q=[]               
        self.a=0                              #variable beacause item counting 
    def add (self,newdata):
        self.q.append(newdata)
        print(self.q)
        self.a+=1

    def delete(self):
        maxv=max(self.q)                     # find max value 
        maxi = self.q.index(maxv)
        del self.q[maxi]                      # remove 
        print(self.q)
        self.a-=1

p1 = pq()
p1.add(12)
p1.add(1)
p1.add(14)
p1.add(17)

while p1.a:             # upto a=0 it will print
    p1.delete()
