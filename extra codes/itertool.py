'''from itertool import product
x =list(product([1,2,3],repeat=2))
print(x)
'''
from itertool import permutations
x = list(permutations([1,2,3],3))
print(x)

# permutations : npr = n!/(n-r)!
''' n = total items
r = arranged items

 n = 3 r = 3 6/1 = 6'''