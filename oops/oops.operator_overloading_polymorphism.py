class A:
    def __init__(self,a):           #intructors
        self.a = a                  # a = 1 , a = 2 
                                    # operator overloading is doing through function overloading
    def __add__(self,o):
        return self.a + o.a         # o = second item and self is first item
                                    # operator over loading + symbol 
ob1 = A(1)
ob2 = A(2)
print(ob1 + ob2)
ob3 = A("geeks")
ob4 = A("for")
print(ob3 + ob4)
