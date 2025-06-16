class calaulation1:
    def summation(self,x,y):
        return x + y
class calcalution2:
    def multiplication(self,x,y):
        return x * y
class derived(calaulation1,calcalution2):
    def divide(self,x,y):
        return x / y

d = derived()
print(isinstance(d,derived))
print(isinstance(d,calaulation1))
print(isinstance(d,calcalution2))