class calaulation1:
    def summation(self,x,y):
        return x + y
class calcalution2:
    def multiplication(self,x,y):
        return x * y
class derived(calaulation1,calcalution2):
    def divide(self,x,y):
        return x / y

d1=derived()
print(issubclass(derived,calaulation1))
print(issubclass(derived,calcalution2))
print(issubclass(calaulation1,calcalution2))