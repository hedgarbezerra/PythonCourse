"""Existem duas formas de fazer um set que só pode existir um elemento, não é possivel ter
duplicatas, lembrando que os sets são parcialmente imutaveis,
 voce pode inserir e remover mas não editar
 Interessante ressaltar que um set criado com {} pode ser confundido com um Dict"""

set1 = {4, 3, 2, 1, 0}
set2 = set({1, 2, 3, 4})
print(f'Set1: {set1} e o Set2 {set2}')

#Adição
set1.add(11)

#update
set2.update([22, 1])
print(f'Set1: {set1} e o Set2{set2}')

#remover
set1.discard(1)
set2.remove(2)
print(f'Set1: {set1} e o Set2{set2}')

#unindo Sets pode ser usado em outras classes, desde que sejam do mesmo tipo, sempre sem repetir elementos
print(set1 | set2)
print(set1.union(set2))

#Interseção / retornando elementos em comum
print(set1 & set2)
print(set1.intersection(set2))

#Oposto de interseção(Diferença)
print(set1 - set2)
print(set1.difference(set2))

#diferença Assimétrica retorna elementos diferentes em ambos
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
