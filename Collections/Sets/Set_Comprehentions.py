""" Set Comprehention é semelhante às listas

"""
set1 = set({i * i for i in range(10)})
set2 = {1, 4, 555, 12}
print(set1)
setx = {i for i in set1.union(set2)}
print(setx)
sett = frozenset([1, 23, 111, 12])
print(sett)
