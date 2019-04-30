from collections import deque
"""Listas podem agir como Pilhas e filas"""

"""Ao utilizar os metodos pop e append podemos fazer com que lsitas ajam como pilhas:"""

pilha = [1, 4, 5, 2, 10]
#removendo do topo
pilha.pop()

#adicionando no topo
pilha.append(3)
print(pilha)

"""Agora com filas"""

fila = deque(['Maria', 'Jose', 'Pedro', 'MAtheus'])
#Adicionando no fim da fila
fila.append('Hedgar')
print(fila)
fila.popleft()
print(fila)
