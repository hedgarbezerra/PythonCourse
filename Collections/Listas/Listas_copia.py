import copy


lista1 = [[1, 2, True], ['Olá Mundo']]

"""Primeiro é a DeepCopy que copia todo conteudo da lista para utra variavel o que não ira
causar mudanças na lista inicial"""
lista_copia = copy.deepcopy(lista1)
print(lista1)
lista1[0][1] = 'A'
print(lista1)

"""Agora a Shallow copy que faz uma cópia da propria lista(usa o objeto armazenado na memória
Caso hajam mudanças nessa cópia irá surtir efeito na lista copiada"""
#lista_copia2 = lista1.copy()
lista_copia2 = copy.copy(lista1)
print(lista_copia2)


