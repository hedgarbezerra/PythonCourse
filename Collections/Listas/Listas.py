lista_simples = [1, 23.3, 13, 99]
print(lista_simples)

"""Insire na lista na ultima posição"""
#lista_simples.append('do carai')

"""Insere em determinada posição (posição , elemento)"""
#lista_simples.insert([12, 3, 109], 9)
print(lista_simples)

"""Este retorna a posição do objeto caso exista"""
print(lista_simples.index(1))

"""Conta o quantidade de objetos na lista e a outra o tamanho da lista no total"""
print(lista_simples.count(2))
print(len(lista_simples))

"""O Pop remove o objeto na posição definida e o remove remove o objeto definido"""
#lista_simples.pop(1)
#lista_simples.remove(9)
print(lista_simples)

"""Sort ordena a lista"""
lista_simples.sort(reverse=True)
print(lista_simples)

