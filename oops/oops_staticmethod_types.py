# static :
# using static method
class mathematics:
    def addnumbers(x,y):
        return x+y
m = staticmethod(mathematics.addnumbers)     #static method syntax --- staticmethod(class_name.function_name)  result is stored in m
print(m(4,44))


#static method by using decorators
class mathematics:
    @staticmethod
    def addnumbers(x,y):
        return x+y
print(mathematics.addnumbers(4,44))
