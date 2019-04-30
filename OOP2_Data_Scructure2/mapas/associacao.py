class Associacao():
    def __init__(self, chave, valor):
        self.__chave = chave
        self.__valor = valor

    @property
    def chave(self):
        return self.__chave

    @property
    def valor(self):
        return self.__valor

    def __str__(self):
        return f'{self.__chave} {self.__valor}'