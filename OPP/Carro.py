from OPP.Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super(Carro, self).__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas

    def pintar(self, value):
        self._cor = value
