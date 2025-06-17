class bank:
    def getroi(self):
        return 10
class sbi(bank):
    def getroi(self):
        return 8
class icici(bank):
    def getroi(self):
        return 9
    
b1 = bank()
print(b1.getroi())
s1 = sbi()
print(s1.getroi())
i1 = icici()
print(i1.getroi())
    
