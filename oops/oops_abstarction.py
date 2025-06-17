from abc import ABC,abstractmethod         # abc class (abstract class - car) is bulit class 
class car (ABC):                           # class car is created ABC ssoo it is single level.
    @abstractmethod                        # @ IS DECORATOR symbol  this method is converting the 
    def milega(self):                      # empty method into abstract method(milega)
        pass
class tesla(car):                          # tesla class lo car is created and in car class the ABC is created so it is multi level 
    def milega(self):
        print("milega is 20kmph")          #abstract method defination method is write in child method
class BMW(car):
    def milega(self):
        print("milega is 12kmph")

t1 = tesla()
t1.milega()
b1=BMW()
b1.milega()
