#dynamic implementations:
#creating the ds using linked list  everu time inserting the data before the 10(right to left(10))
class queue:                                  #creating node  for
    def __init__(self,dataval):
        self.dataval = dataval             
        self.nextval = None 
                                       #address
class dynamic:                             # for linked list 
    def __init__(self):
        self.front = None
        self.rare = None

    def enque(self,newdata):
        newnode = queue(newdata)                          #node is monday
        if self.front is None:
            self.front = newnode                    #newnode 
            self.rare = newnode
        else:
            self.rare.nextval = newnode
            self.rare = newnode
            newnode.nextval=self.front                      #1000 ois storde in newnoode()
    
    def deque(self):
        if self.front is None:
            print("empty")
        elif self.front == self.rare:
            x=self.front.dataval
            self.front.dataval = 0
            self.front = None
            self.rare = None
        else:
            x=self.front.dataval
            self.front.dataval = ''
            self.front = self.front.nextval
            return x
        
    def display(self):
        if self.front is None:
            print("empty")
        else:
            temp = self.front
            while(temp):
                print(temp.dataval,end=" ")
                temp = temp.nextval
                if(temp==self.front):
                    break
            print()

q1=dynamic()
while True:
    print("enque <value>")
    print("deque")
    print("display")
    print("quit")
    do = input("what would u like to do? ").split()
    operation = do[0].strip().lower()
    if operation == 'enque':
        q1.enque(int(do[1]))
    elif operation == 'deque':
        popped = q1.deque()
        if popped is None:
            print("queue is empty")
        else:
            print("popped value: ",int(popped))
    elif operation == "display":
        q1.display()
    elif operation == "quit":
        break
