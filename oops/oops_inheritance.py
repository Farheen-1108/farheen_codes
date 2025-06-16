# single level inheritance
class father:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)

class son(father):
    def __init__(self, name):
        self.name = name
    def show1(self):
        print(self.name)

x=father("ram")
x.show()
y=son("yash")
y.show1()
y.show()              # with child y and show the parent  (here chid class can use parens class)
x.show()               # if we write a parents class cannot use child class

#exampless:
class science:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)

class biotech(science):
    def __init__(self, name):
        self.name = name
    def show1(self):
        print(self.name)

x=father("subject")
x.show()
y=son("sub_section")
y.show1()
y.show()              # with child y and show the parent  (here chid class can use parens class)
x.show()              # if we write a parents class cannot use child class

#singlelevel inheritance
class base :
    def __init__(self):
        self._a=32
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)                  #no need of identation because of def inside the def
        print(self._a+2)

x = base()
y = derived()
print(x._a)                               # piublic and protected data can be used anywhere
print(y._a)                               # inheritance proofed data

#multi level inheritance
class base :
    def __init__(self):
        self._a=32
        print(self._a)

class derived(base):
    def __init__(self):
        base.__init__(self)                  #no need of identation because of def inside the def
        print(self._a+2)
    
class derived1(derived):                           # derived is the class
    def __init__(self):
        derived.__init__(self)
        print(self._a*2)
x = derived1()

#multiple inheritance:
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
s1=son1()
s1.son1name="yash"
s1.fathername="ram"
s1.mothername="sita"
s1.Son1information()

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
