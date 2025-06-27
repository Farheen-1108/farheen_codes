#dynamic implementations:
#creating the ds using linked list  everu time inserting the data before the 10(right to left(10))
class stack:                                  #creating node  for
    def __init__(self,dataval):
        self.dataval = dataval             # 12
        self.nextval = None 
                                       #address
class dynamic:                             # for linked list 
    def __init__(self):
        self.top = None

    def push(self,newdata):
        newnode = stack(newdata)                          #node is monday
        if self.top is None:
            self.top = newnode                    #newnode 
        else:
            newnode.nextval=self.top                      #1000 ois storde in newnoode()
            self.top = newnode
    
    def pop(self):
        if self.top is None:
            print("empty")
        else:
            x=self.top.dataval
            self.top = self.top.nextval
            return x
        
    def display(self):
        if self.top is None:
            print("empty")
        else:
            temp = self.top
            while(temp):
                print(temp.dataval,end=" ")
                temp = temp.nextval
            print()
s1=dynamic()
s1.top=stack(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()