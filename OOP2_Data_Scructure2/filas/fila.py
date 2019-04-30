from listas import lista_ligada

class Fila():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()

    def enfileirar(self, elemento):
        self.__elementos.inserir(elemento)

    def esta_vazia(self):
        return self.__elementos.esta_vazia()

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        resultado = self.__elementos.recuperar_elemento_no(0)
        self.__elementos.remover_posicao(0)
        return resultado

    def __str__(self):
        temp = self.__elementos.__str__()
        return temp