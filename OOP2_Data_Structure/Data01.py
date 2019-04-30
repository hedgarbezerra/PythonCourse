from OOP2_Data_Structure import Vetor
from OOP2_Data_Structure import Node, Lista_ligada, Node_duplo, Lista_dupla_ligada

print(30*"-", 'MENU', 30*'-')
print('1 - Vetor\n2 - Listas Ligadas\n3 - Lista duplamente ligada')
menu = 3
#int(input('Insira a opção desejada: \n'))
if menu == 1:
    vetor_int = Vetor.Vetor(3)
    vetor_int.inserir_final(1)
    vetor_int.inserir_final(99)
    vetor_int.inserir(3, 1)
    vetor_int.inserir_final(83)
    print(vetor_int.listar(2))
    print(vetor_int.vetor_tamanho())
    print(vetor_int)
    print(vetor_int.remover_elemento_index(2))
    print(vetor_int)

elif menu == 2:
    node1 = Node.Node(1)
    lista = Lista_ligada.Listaligada()
    lista.inserir(12)
    lista.inserir(3)
    lista.inserir(33)
    lista.inserir(11)
    lista.inserir_posicao(14, 4)
    print(lista)
    print(lista.indice(12))
    print(lista.contem(3))
    print(lista.node_posicao(0))
    lista.remover_posicao(1)
    print(lista)
elif menu == 3:
     print('a')


