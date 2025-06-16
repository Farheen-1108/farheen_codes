class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1=person("fara",20)               
print(getattr(p1,"name"))          # get attribute
print(getattr(p1,"age"))

setattr(p1,"age",21)               # set attribute  this set attribute 
print(getattr(p1,"age"))           # can change the values modify them by using set 

print(hasattr(p1,"age"))           # has attribute
print(hasattr(p1,"id"))

