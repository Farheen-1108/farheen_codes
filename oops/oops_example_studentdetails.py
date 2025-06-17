class student:
    def __init__(self,name,rollno,maths_marks,physics_marks,chem_marks):
                self.name = name
                self.rollno = rollno                           # intialized the method 
                self.maths_marks = maths_marks
                self.physics_marks = physics_marks
                self.chem_marks = chem_marks

    def calcualtion(self):
        if(self.maths_marks>=40 and self.physics_marks>=40 and self.chem_marks>=40):
            total = self.maths_marks + self.physics_marks + self.chem_marks 
            avg = total/3
            print(total)
            print(avg)
            if (self.maths_marks>75 and self.physics_marks>75) or (self.physics_marks>75 and self.chem_marks>75) or (self.chem_marks>75 and self.maths_marks>75):
                print("admission is confirmed")
            else:
                print("admission is not confirmed")
        else:
             print("fail")

s1 = student("farheen",108,97,94,95)
s1.calcualtion()
