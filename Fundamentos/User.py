class User:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def data(self):
        print(f'Olá, sou {self.nome}, tenho {self.idade} anos e {self.altura} metros de altura!')

