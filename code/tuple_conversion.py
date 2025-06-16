n = int(input("enter the int value: "))
f = float(input("enter the flo num: "))
s = input("enter the str: ")

print("before conversion of integer:")
print("after coversion of string:",str(n))
print("after coversion of float:",float(n))
print("after coversion of complex:",complex(n))

print("before conversion of float:")
print("after coversion of string:",str(f))
print("after coversion of float:",int(f))
print("after coversion of complex:",complex(f))

print("before conversion of string:")
print("after coversion of int:",int(s))
print("after coversion of float:",float(s))
print("after coversion of list:",list(s))
print("after coversion of tuple:",tuple(s)) 