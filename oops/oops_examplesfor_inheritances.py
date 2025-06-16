#multi level inheritance
class house:
    def __init__(self):
        self._a=44
        print(self._a)

class derived(house):
    def __init__(self):
        house.__init__(self)                  #no need of identation because of def inside the def
        print(self._a+2)
    
class derived1(derived):                           # derived is the class
    def __init__(self):
        derived.__init__(self)
        print(self._a*2)
x = derived1()

#multiple inheritance:
class university:
    uniname=''
    def UNIVERSITY(self):              #class name and method name is not same 
        print(self.uniname)

class branch:
    branchname=''
    def BRANCH(self):
        print(self.branchname)

class dept1(university,branch):
    deptname = ''
    def deptinformation(self):
        print(self.uniname)
        print(self.branchname)
        print(self.deptname)
s1=dept1()
s1.deptname="biotech"
s1.uniname="vignan"
s1.branchname="btech"
s1.deptinformation()

#hierarcy inheritance: not just herarcial but also hybrid also can be complete
class father:
    fathername=''
    def FATHER(self):              #class name and method name is not same 
        print(self.fathername)

class mother:
    mothername=''
    def MOTHER(self):
        print(self.mothername)

class son1(father,mother):
    son1name = ''
    def Son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)

class son2(father,mother):
    son2name = ''
    def Son2information(self):
        print(self.fathername)
        print(self.son2name)

s1=son1()
s1.son1name="yash"
s1.fathername="ram"
s1.mothername="sita"
s1.Son1information()
s2=son2()
s2.son2name="Jash"
s2.fathername="ram"
s2.Son2information()

# hierarcial:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Bird(Animal):
    def speak(self):
        print("Chirp!")

# Creating instances
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

# Calling methods
dog.speak()
cat.speak()
bird.speak()