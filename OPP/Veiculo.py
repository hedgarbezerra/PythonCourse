import abc
import OPP.InterfaceVeiculos


class Veiculo(OPP.InterfaceVeiculos.InterfaceVeiculos, abc.ABC):
    """"O ABC é a library padrão do Python que fornece a Abstração"""
    """Classe treino da TreinaWEb ORientação a objetos"""
    """"O encapsulamento dos atributos devem ser feitos com _  um _ significa protected e dois __ private"""
    def __init__(self, cor: object, tipo_combustivel: object, potencia: object) -> object:
        self._cor = cor
        self._tipo_combustivel = tipo_combustivel
        self._potencia = potencia
        self._qtd_combustivel = 0
        self._is_ligado = False
        self._velocidade = 0

    def __del__(self):
        return 'Objeto foi destruído'

    @property
    def qtd_combustivel(self):
        return self._qtd_combustivel

    @qtd_combustivel.setter
    def qtd_combustivel(self, value):
        pass

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, value):
        pass

    @property
    def cor(self):
        return self._cor
  
    @abc.abstractmethod
    def pintar(self, value):
        self._cor = value

    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, value):
        pass

    def abastecer(self, valor):
        self._qtd_combustivel += valor

    def ligar(self):
        if self._is_ligado:
            return 'Veiculo já está ligado'
        else:
            self._is_ligado = True
            return 'Veiculo ligado'

    def desligar(self):
        if not self._is_ligado:
            return 'Veiculo já está desligado'
        else:
            self._is_ligado = False
            return 'Veiculo desligado'

    def data(self):
        return f' Você tem um veiculo {self._cor} com uma potência de {self._potencia} atualmente com' \
            f' {self._qtd_combustivel} litros de {self._tipo_combustivel}'

    def acelerar(self):
        self._velocidade += 10
