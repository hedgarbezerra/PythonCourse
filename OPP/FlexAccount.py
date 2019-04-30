import OPP.Account


class FlexAccount(OPP.Account.Account):

    def saque(self, value):
        self._saldo -= value
        return f'Foram sacados: R${value}'

    def deposito(self, value):
        self._saldo += value
        return f'Foram depositados: R${value}'

