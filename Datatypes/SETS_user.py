set = {"python","java","sql","js","angularjs","nodejs"}
print(set)
print(type(set))

#accessing the set item:
print("sql" in set)

#adding itms:
set.add("c")
set.add("nodejs")
set.add("expressjs")
print(set)

#update:
set.update(["c++","dbms"])
print(set)

#remove:
set.remove("nodejs")
print(set)

#pop:
set.pop()
print(set)

#discard will not raise error if the items is not present:
set.discard("angularjs")
print(set)

#clear:
set.clear()
print(set)

#union
set1 = {1,2,3,4,5}
set2 = {3,4,5}
print(set1 | set2)

#intersection
print(set1 & set2)

#difference
dm = set1.difference(set2)
print(dm)

#issubset:
issub = set1.issubset(set2)
print(issub)

#issuperse6t
sub = set1.issuperset(set2)
print(sub)