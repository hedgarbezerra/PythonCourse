from OOP2_Data_Structure.Node_duplo import Node_duplo

class Lista_dupla_ligada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0

    def inserir_posicao(self, elemento, posicao):
        if posicao == 0:
            node = Node_duplo(elemento)
            node.proximo = self.__primeiro
            self.__primeiro.anterior = node
            self.__primeiro = node
        elif posicao >= self.__tamanho:
            node = Node_duplo(elemento)
            self.__ultimo.proximo = node
            node.anterior = self.__ultimo
            self.__ultimo = node
        else:
            node_ant = self.node_posicao(posicao -1)
            node_att = self.node_posicao(posicao)
            node = Node_duplo(elemento)
            node_ant.proximo = node
            node.proximo = node_att
            node.anterior = node_ant
        self.__tamanho += 1


    def inserir(self, elemento):
        node = Node_duplo(elemento)
        if self.isVazio():
            self.__primeiro = node
            self.__ultimo = node
        else:
            self.__ultimo.proximo = node
            node.anterior = self.__ultimo
            self.__ultimo = node
        self.__tamanho +=1

    def contem(self, elemento):
        for i in range(self.__tamanho):
            node = self.node_posicao(i)
            if elemento == node.elemento:
                return True
        return False

    def remover_elemento(self, elemento):
        node_rem = self.indice(elemento)
        if node_rem == -1:
            return 'Elemento não existe'
        self.remover_posicao(node_rem)

    def remover_posicao(self, posicao):
        if posicao == 0:
            node_prx = self.__primeiro.proximo
            self.__primeiro.proximo = None
            self.__primeiro.anterior = None
            self.__primeiro = node_prx
        elif posicao == self.__tamanho -1:
            node_pen = self.__ultimo.anterior
            node_pen.proximo = None
            self.__ultimo.anterior = None
            self.__ultimo = node_pen
        else:
            node_rem = self.node_posicao(posicao)
            node_ant = node_rem.anterior
            node_prox = node_rem.proximo
            node_ant.proximo = node_prox
            node_prox.anterior = node_ant
            node_rem.anterior = None
            node_rem.proximo = None
        self.__tamanho -= 1


    def indice(self, elemento):
        for i in range(self.__tamanho):
            node = self.node_posicao(i)
            if node.elemento == elemento:
                return i
        return -1
    def isVazio(self):
        return self.__tamanho == 0

    def __str__(self):
        temp = self.__primeiro
        elementos = ''
        while temp:
            elementos = f'{elementos} {temp.elemento} -'
            temp = temp.proximo
        return elementos


    def node_posicao(self, posicao):
        resultado = 0
        if posicao > self.__tamanho:
            return 'Posição vazia'
        else:
            for i in range(posicao+1):
                if i == 0:
                    resultado = self.__primeiro
                else:
                    resultado = resultado.proximo
            return resultado

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, value):
        self.__tamanho = value
