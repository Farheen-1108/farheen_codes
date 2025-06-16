class person:     # class creation 
    age = 36

p1 = person()       # object creation
print(p1.age)       # connecting both the class and object
# when a data can be used by  total objects of a class then that is called static variables.
p2 = person()
print(p2.age)
print(person.age)

# different varbles need for  instance variable
