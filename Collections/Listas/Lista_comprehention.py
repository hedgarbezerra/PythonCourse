lista = [1, 2, 3, 4, 5, 6]
lista2 = []
for i in lista:
    lista2.append(i*i)
print(lista2)

comprehention = str([i*i for i in lista])
print(comprehention)

