import abc


class InterfaceVeiculos(abc.ABC):

    @abc.abstractmethod
    def pintar(self, value):
       pass

    @abc.abstractmethod
    def abastecer(self, valor):
        pass

    @abc.abstractmethod
    def ligar(self):
        pass

    @abc.abstractmethod
    def desligar(self):
        pass

    @abc.abstractmethod
    def data(self):
        pass

    @abc.abstractmethod
    def acelerar(self):
        pass

