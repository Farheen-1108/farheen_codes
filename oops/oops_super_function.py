class base :
    def __init__(self):                    # in this the base is parent for the drevied child
        self._a=32
        print(self._a)

class derived(base):                        # in this the the derived is parent for deriverd1 child
    def __init__(self):
        super().__init__()                  #no need of identation because of def inside the def
        print(self._a+2)
    
class derived1(derived):                           # derived is the class
    def __init__(self):                            
        super().__init__()
        print(self._a+3)
x = derived1()
