class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho # [None], [None], [None]
        self.__posicao = 0

    def tamanho_vetor(self):
        return len(self.__elementos)

    def __str__(self):
        # 1 2 3 4
        return ' '.join([ str(i) for i in self.__elementos])

    def contem(self, elemento):
        # 1, 2, 4, 3
        # 5
        for i in range(self.tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elem == elemento:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elem == elemento:
                return i
        return -1

    def inserir_elemento_posicao(self, elemento, posicao):
        # 1, 2, 3
        # 1, 2, 4, 3
        # 1, 2, 4 vetor_inicio
        # 3 vetor_final
        # 2
        vetor_inicio = self.__elementos[:posicao] + [None] #1, 2, [None]
        vetor_final = self.__elementos[posicao:] #3
        vetor_inicio[len(vetor_inicio) - 1] = elemento #1, 2, 4, 3
        self.__elementos = vetor_inicio + vetor_final #1, 2, 4, 3
        self.__posicao += 1

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= self.tamanho_vetor():
            # [None], [None], [None]
            self.__elementos = self.__elementos + [None]
            # [None], [None], [None], [None]
        # 1, 2, 3
        # 4
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def remover_elemento_indice(self, posicao):
        # 1, 2, 3
        # 1, vetor_inicio
        # 3 vetor_final
        # 1
        vetor_inicio = self.__elementos[:posicao] # 1 2 5 vetor_inicio
        vetor_final = self.__elementos[posicao + 1:] # 3 1 vetor_final
        self.__elementos = vetor_inicio + vetor_final # 1 2 5 3 1
        self.__posicao -= 1

    def remover_elemento(self, elemento):
        posicao = self.indice(elemento)
        self.remover_elemento_indice(posicao)

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]