class person:
    def __init__(self,name,age):  #two parameters only present 
        self.name = name          #writing class part 
        self.age = age

#object creations:
p1=person("farheen",20)
p2=person("lalitha",21)

print(p1.name,p1.age)
print(p2.name,p2.age)

#what we write in parameter we have to write in class  anything can be write

class person:
    def __init__(se,name,age):  #two parameters only present 
        se.name = name          #writing class part 
        se.age = age

#object creations:
p1=person("farheen",20)
p2=person("harshi",21)

print(p1.name,p1.age)
print(p2.name,p2.age)

#without constructor:
class person:
    name = "farheen"
    age = 20
    print(name,age)
person()

# for many without constructor:

class person:
    name = ''
    age = ''
p1=person()
p1.name='farheen'
p1.age=20
print(p1.name,p1.age)

#not printing too many statements:
class person:
    def __init__(se,name,age):  #two parameters only present 
        se.name = name          #writing class part # special method
        se.age = age

    def printing(self):                 #normal method
        print(self.name,self.age)

#object creations:
p1=person("farheen",20)
p2=person("harshi",21)
p1.printing()                       #calling function
p2.printing()
