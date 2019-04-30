
def exe1():
    valor = float(input("Insira o valor desejado: \n"))
    print("O valor final da conversão foi: ", valor*3.85)


def exe2():
    comprimento = int(input("Insira o comprimento do seu retângulo: \n"))
    altura = int(input("Insira altura do seu retângulo: \n"))
    print("A àrea do seu retângulo é: ", (comprimento * 2) + (altura * 2))

def exe4():
    entrada = input("Insira uma palavra: \n").upper()
    while entrada != 'PARAR':
        print('Existem :', entrada.count('I'), ' na palavra: ', entrada, '\n')
        entrada = input("Insira uma palavra: \n").upper()
    print('Usuário parou a execução!\n')

if __name__ == '__main__':
    exe4()

