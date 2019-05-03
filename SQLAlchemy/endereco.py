class Endereco:
    def __init__(self, bairro, cep, logradouro, cidade, uf):
        self.bairro = bairro
        self.cep = cep
        self.logradouro = logradouro
        self.cidade = cidade
        self.uf = uf

    def __str__(self):
        return f'O CEP {self.cep} representa o endereço {self.logradouro} no bairro {self.bairro} em {self.cidade}-{self.uf} '

