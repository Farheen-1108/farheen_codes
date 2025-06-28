'''n = int(input("enyer the num:"))
fact = 1
for i in range (1,n+1):
    fact = fact*i
print(fact)'''

year = int(input())
if (year%4 == 0 and year%100!=0) or (year%400 == 0):
    print(True)
else:
    print(False) 

def is_leap(year):
    leap = True
    not_leap = False
    if (year%4 == 0 and year%100!=0) or (year%400 == 0):
        return leap
    else:
        return not_leap
year = int(input())
print(is_leap(year))