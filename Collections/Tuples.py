"""Tuplas recebem quaisquer tipos de dados porém eles são imutaveis após a criação,
sendo assim não podem ser removidos ou inseridos valores.
além de podemos usar .index() e .count()"""
tuple1 = (1, 2, 4, 'Olá', 2.1, False, 1)
tuple2 = (11, 112, 1)
print(tuple1)
print(type(tuple1))
print(tuple1.count(1))
print(tuple1.index(1))
#Verificando a existencia de um valor em uma tupla
print(2 in tuple1)
#Concat tuples durante impressão
print(tuple1.__add__(tuple2))

