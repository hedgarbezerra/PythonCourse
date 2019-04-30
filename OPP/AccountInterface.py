"""Duck-typing é semelhante ao conceito de interfaces,
você define uma classe abstrata com ABC e define métodos obrigatorios"""
import abc


class AccountInterface(abc.ABC):

    @abc.abstractmethod
    def deposito(self):
        pass

    @abc.abstractmethod
    def saque(self):
        pass

    @abc.abstractmethod
    def saldo(self):
        pass

    @abc.abstractmethod
    def congelar_conta(self):
        pass
