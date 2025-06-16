class student:
    def __init__(self,name,rollno,maths_marks,physics_marks,chem_marks):
                self.name = name
                self.rollno = rollno
                self.maths_marks = maths_marks
                self.physics_marks = physics_marks
                self.chem_marks = chem_marks

    def printing(self):                 
        print(self.name,self.rollno,self.maths_marks,self.physics_marks,self.chem_marks)

class calculations:
    def summation(self,maths_marks,physics_marks,chem_marks):
        cal = ( maths_marks + physics_marks + chem_marks ) /3
        return cal

    def decide(self):
        if (self.maths_marks>75 and self.physics_marks>75):
            print("eligible")
        elif (self.physics_marks>75 and self.chem_marks>75):
            ( "eligible")
        elif (self.chem_marks>75 and self.maths_marks>75):
            print("eligible")
        else:
            print("not eligible")

