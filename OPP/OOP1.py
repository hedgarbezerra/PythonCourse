import OPP.Carro
import OPP.Moto
import OPP.Veiculo
from OPP import FlexAccount, User, GoldenAccount

moto = OPP.Moto.Moto('Preta', 'Gasolina', 300, 2)
carro1 = OPP.Carro.Carro('Azul', 'Gasolina', 2.0, 4)
conta1 = FlexAccount.FlexAccount(12344, 1233)
conta2 = GoldenAccount.GoldenAccount(12199, 14011)
usuario = User.User('Hedgar', 22, '771-122-121-43', 'Rua X', 12344,1233, 'golden')
usuario2 = User.User('Matheus', 25, '722-111-991-43', 'Rua 8', 12199, 14444, 'flex')

if __name__ == '__main__':
    print(usuario.name)
    print(usuario.accout.isAtiva)
    print(usuario.accout.saldo())
    print(usuario.accout.deposito(20))
    print(usuario.accout.saldo())
    print(40*'-')
    print(usuario2.name)
    print(usuario2.accout.isAtiva)
    print(usuario2.accout.saldo())
    print(usuario2.accout.deposito(20))
    print(usuario2.accout.saldo())
    print(usuario2.accout.saque(2))
    print(usuario2.accout.saldo())
    #carro1.abastecer(80)
    #print(carro1.data())
    #print(carro1.desligar())
    #print(carro1.ligar())
    #print(moto.data())