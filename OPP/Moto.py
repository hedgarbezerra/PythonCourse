from OPP.Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passa):
        super(Moto, self).__init__(cor, tipo_combustivel, potencia)
        self.__qtd_passageiros = qtd_passa

    def pintar(self, value):
        self._cor = value


