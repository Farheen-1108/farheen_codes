#MRO (METHOD RESOLUTION ORDER)

class A:
    def myname(self):                  #self is same for all threee so it is called as hieraracy
        print("i am class A")
class B(A):                            # myname is same for all three so it is called as method resolution order / method overriding
    def myname(self):
        print("i am class B")                  
class C(A):
    def myname(self):
        print("i am class C")
class D(B,C):                          # both B,C is given in calling function so it is multiple
    pass                               # as we got the both multiple and hieraracy so it is also hybrid inheritance
d=D()
d.myname()



class A: 
    def myname(self):
        print("i am class A")
class B(A):
    def myname(self):
        print("i am class B")
class C(A):
    def myname(self):
        print("i am class C")
class D(B,C):
    pass
d = D()
print(D.__mro__)                     # tuple
print(D.mro())                       #list
