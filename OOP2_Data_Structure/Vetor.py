class Vetor:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def __str__(self):
        """Juntando os elementos em um loop com um string ' - '"""
        return ' - '.join([str(i) for i in self.__elementos])

    def contem(self, elemento):
        """Possível fazer com loop com a  for i in
        range(len(elemento))"""
        return self.__elementos.__contains__(elemento)

    def indice(self, elemento):
        """Possível fazer com loop com a  for i in
                range(len(elemento)) e então retornar a posicao"""
        try:
            return self.__elementos.index(elemento)
        except:
            return 'Elemento não existe no vetor'

    def remover_elemento(self, elemento):
        try:
            self.__elementos.remove(elemento)
            #self.__elementos.pop(posicao)
        except:
            return 'O elemento não existe no vetor'

    def remover_elemento_index(self, posicao):
        try:
            self.__elementos.pop(posicao)
        except:
            return 'A posição está vazia'

    def inserir(self, elemento, posicao):
        """
        Dado um vetor de tamanho três, será feito um split
        Onde :posicao ira pegar os elementos ate a determinada posicao
        E posicao: todos elementos depois da posicao """
        vetor_inicio = self.__elementos[:posicao]+[None]
        vetor_fim = self.__elementos[posicao:]
        vetor_inicio[len(vetor_inicio) - 1]  = elemento
        self.__elementos = vetor_inicio + vetor_fim
        self.__posicao += 1

    def vetor_tamanho(self):
        return len(self.__elementos)

    def inserir_final(self, elemento):
        if self.__posicao >= self.vetor_tamanho():
            self.__elementos = self.__elementos + [None]
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar(self, posicao):
        return self.__elementos[posicao]
