class myclass:    # created class
    x = 5
print(myclass)

p1 = myclass       # created objects using the help of classes
print(p1.x)        # object name = p1 and printed the value x

''' __init__() it is constructor or initializer (bulit in function)
 all classes have a function called -- __init__()  always exceuted 
 when class is exceuted  , used to assign a value to object properties\
 The __init__() function is called automatically every time the
 class is being used to create a new object.'''

''' The self parameter is a reference to the current instance of the class,
 and is used to access variables that belong to the class.'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("fara",20)           # p1 is object name ((in object the objectname = classname))
print(p1.name)
print(p1.age)

# __str__()  function when class are in string
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = person("farheen",19)
print(p1)
             
# object can also cantain method(function),

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):                       #object method is used here inside the object
        print ("Hello my name",self.name)
    
p1 = person("fara",21)
p1.myfunc()                                  # () are main to call the function
print(p1.age)

# pass :
''' class definitions cannot be empty, but if you for some reason have a class 
definition with no content, put in the pass statement to avoid getting an error.
'''
# inheritance:
''' it defines a class that inherits all the methods and properties from anothe 
class
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''
# create parent class:
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

p1 = person("tasneem","khutija")
p1.printname()

#child class
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(person):
    pass

p1 = Student("tasneem","khutija")
p1.printname()


class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(person):
    def __init__(self, fname, lname):
        person.__init__(self,fname, lname)

p1 = Student("tasneem","khutija")
p1.printname()

'''super() Function
Python also has a super() function that will 
make the child class inherit all the methods and properties from its parent:
super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.'''

class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

p1 = Student("mohammad","khutija")
p1.printname()

#add properties:

class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.gradutaion = 2026

p1 = Student("mohammad","farheen")
print(p1.gradutaion)

#add properties items:
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class student(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.gradutaion = year
    
    def welcome(self):
        print("Welcome", self.fname, self.lname, "is the", self.gradutaion) 

p1 = student("mohammad","farheen",2026)
p1.welcome()

# polymorphism :
''' means -- "many forms" in programming it refers too method function and 
operator with same name that can be exceuted on many onjects or classes
'''
# on different objects len() function:
# strings:
x = "Hello World"
print(len(x))

#tuples:
t = ("fruits","cars","books","vehicles")
print(len(t))

#dictionary:
d = {"brand": "lamborigini", "phn_model" : "iphone_18", "tablets" : "ipad"}
print(len(d))

#class polymorphism:
''' Polymorphism is often used in Class methods, where we can have multiple 
    classes with the same method name.
For example, say we have three classes: Car, Boat, and Plane, and they all
    have a method called move() '''

# DIFFERENT CLASSES WITH SAME METHODS:

class car:
    def __init__(self,cname,cyear):
        self.name = cname
        self.year = cyear
    def move(self):
        print("travels with the speed of 40kmph.")

class phone:
    def __init__(self,pname,pversion):
        self.name = pname
        self.version = pversion
    def move(self):
        print("the latest version of iphone.")

class food:
    def __init__(self,fname,fcost):
        self.fname = fname
        self.fcost = fcost
    def move(self):
        print("the cost of food and name.")

car1 = car("lamborigini",2022)
phone1 = phone("iphone",3.3)
food1 = food("chinese",100)

for x in (car1,phone1,food1):
    x.move()

# inheritance class polymorphism:
''' Yes. If we use the example above and make a parent class called Vehicle, 
and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the 
Vehicle methods, but can override them:'''

#Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class vehicle:
    def __init__(self,brand,model):         #same method for all classes.
        self.brand = brand
        self.model = model
    def move(self):
        print("move!")

class car(vehicle):
    def move(self):
        print("car fasts the speed")

class boat(vehicle):
    def move(self):
        print("sail the boat")

class plane(vehicle):
    def move (self):
        print("fly in sky")

car1 = car("lamborigini","latest")
boat1 = boat("titanic","old")
plane1 = plane("air india","touring")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
        # concepts of classes ,objects
    ''' inheritance , polymorhphism...etc topics related'''
