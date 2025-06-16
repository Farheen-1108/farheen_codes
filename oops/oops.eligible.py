class person:
    def __init__(se,name,age):  #two parameters only present 
        se.name = name          #writing class part # special method
        se.age = age

    def printing(self):                 #normal method
        print(self.name,self.age)

    def decide(self):
        if (self.age>18):
            print("eligible / major")
        else:
            print("not eligible / minor")

    def uppercaseconversion(self):  #class inside that method
        x=self.name
        print(x.upper())                   
        # print(self.name.upper())
    def lenght(self):
        print(len(self.name))

#object creations:
p1=person("farheen",20)
p2=person("harshi",12)
p1.printing()                       #calling function
p2.printing()
p1.decide()
p2.decide()
p1.uppercaseconversion()
p2.uppercaseconversion()
p1.lenght()
