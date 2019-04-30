from listas import lista_ligada
from espalhamento import tabela_espalhamento

class Conjunto():
    def __init__(self):
        self.__elementos = tabela_espalhamento.TabelaEspalhamento()

    def inserir(self, elemento):
        self.__elementos.inserir(elemento)
    #
    # def inserir_posicao(self, posicao, elemento):
    #     if not self.contem(elemento):
    #         self.__elementos.inserir_posicao(posicao, elemento)
    #         return True
    #     return False

    def __str__(self):
        return self.__elementos.__str__()

    def contem(self, elemento):
        return self.__elementos.contem(elemento)
    #
    # def indice(self, elemento):
    #     return self.__elementos.indice(elemento)

    def esta_vazia(self):
        return self.__elementos.tamanho == 0

    # def recuperar_elemento_no(self, posicao):
    #     return self.__elementos.recuperar_elemento_no(posicao)

    # def recuperar_no(self, posicao):
    #     return self.__elementos.recuperar_no(posicao)
    #
    # def tamanho(self):
    #     return self.__elementos.tamanho
    #
    # def remover_posicao(self, posicao):
    #     self.__elementos.remover_posicao(posicao)

    def remover_elemento(self, elemento):
        self.__elementos.remover(elemento)