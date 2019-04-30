import abc
import OPP.AccountInterface


class Account(OPP.AccountInterface.AccountInterface, abc.ABC):

    def __init__(self, numero, agencia):
        self._saldo = 0
        self._isAtiva = True
        self._numero = numero
        self._agencia = agencia

    def __del__(self):
        return 'Conta encerrada'

    @abc.abstractmethod
    def deposito(self):
        pass

    @abc.abstractmethod
    def saque(self):
        pass

    def saldo(self):
        return self._saldo

    def congelar_conta(self):
        self._isAtiva = False
        return 'Sua conta foi congelada!'

    @property
    def isAtiva(self):
        return self._isAtiva

    @isAtiva.setter
    def isAtiva(self, value):
        self._isAtiva = value

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

