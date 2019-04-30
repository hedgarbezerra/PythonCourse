"""Ranges são elementos para iteração no Python
podemos definir os passos e o inicio das seguintes formas:"""

#Esse é o limite da minha tupla que por padrão irá incremente de 1 em 1
rang = range(10)
for i in rang:
    print(i)
print(30*'-')
#Podemos definir o número inicial adicionando mais um número
rang1 = range(1, 10)
for i in rang1:
    print(i)
print(30*'-')
#Aqui definimos o número inicial também como o máximo e o passo(3)
rang2 = range(0, 10, 3)
for i in rang2:
    print(i)

