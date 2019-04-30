from OPP import GoldenAccount, FlexAccount


class User:
    def __init__(self, name, age, cpf, address, numero, agencia, tipo):
        self.__name = name
        self.__age = age
        self.__cpf = cpf
        self.__address = address
        if tipo.upper() == 'FLEX':
            self.__account = FlexAccount.FlexAccount(numero, agencia)
        elif tipo.upper() == 'GOLDEN':
            self.__account = GoldenAccount.GoldenAccount(numero, agencia)
        else:
            pass

    @property
    def accout(self):
        return self.__account

    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf

    @property
    def age(self):
        return self.__age

    @property
    def address(self):
        return self.__address


