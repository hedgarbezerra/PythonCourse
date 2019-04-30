import OPP.Account


class GoldenAccount(OPP.Account.Account):

    def saque(self, value):
        self._saldo -= value
        return f'Foram sacados: R${value}'

    def deposito(self, value):
        self._saldo += value + (value*10/100)
        return f'Foram depositados: R$ {value} onde foi concebido' \
            f' um bonus de: R$ {value * 10 / 100}'
