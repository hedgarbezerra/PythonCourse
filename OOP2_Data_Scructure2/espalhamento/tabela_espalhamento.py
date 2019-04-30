from  listas import lista_ligada

# 0: 10, 100, 1000
# 1: 15, 25, 35,
# 2: 16, 26, 36
# 3 (150:200):
class TabelaEspalhamento():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()
        self.__numero_categorias = 10
        self.__tamanho = 0

        for i in range(self.__numero_categorias):
            self.__elementos.inserir(lista_ligada.ListaLigada())

    @property
    def tamanho(self):
        return self.__tamanho

    def __gerar_numero_espalhamento(self, elemento):
        return hash(elemento) % self.__numero_categorias

    def inserir(self, elemento):
        if self.contem(elemento):
            return False
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        categoria.inserir(elemento)
        self.__tamanho += 1
        return True

    def remover(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        categoria.remover_elemento(elemento)
        self.__tamanho -= 1

    def contem(self, elemento):
        numero_espalhamento = self.__gerar_numero_espalhamento(elemento)
        categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
        return categoria.contem(elemento)

    def __str__(self):
        return self.__elementos.__str__()