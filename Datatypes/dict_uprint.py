jobrole={101:"f_e_d",102:"b_e_d",103:"sql_d"}
print(jobrole)
print(type(jobrole))

#accessing using key values
print(jobrole[101])
print(jobrole[102])
print(jobrole[103])

#modifying:
jobrole[101]="ui/ux_d"
print(jobrole)

#add an element to dict:
jobrole[104] = "data_e"
jobrole[105] = "python_d"
jobrole[106] = "data_ana"
print(jobrole)

#deleting:
jobrole.pop(101)
del jobrole[103]
print(jobrole)

#length:
print(len(jobrole))

#keys:
print(jobrole.keys())

#value:
print(jobrole.values())

#items:
print(jobrole.items())

#update:
a = {108:"java_del"}
jobrole.update(a)
print(jobrole)

#fromkeys:
keys={109,110}
values="dsa","js"
print(jobrole.fromkeys(keys,values))

