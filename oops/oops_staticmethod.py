class mathematics:
    def addnumbers(x,y):
        return x+y
m = staticmethod(mathematics.addnumbers)     #static method syntax --- staticmethod(class_name.function_name)  result is stored in m
print(m(4,44))
