import math


def exe1():
    mat = int(input('Insira um numero para calcular o fatorial: \n'))
    print(math.factorial(mat))


def exe2():
    mat = int(input('Insira um numero para saber se é impar ou par: \n'))
    if mat % 2 == 0:
        print('O número ', mat, 'é par')
    else:
        print('O número ', mat, 'é impar')


if __name__ == '__main__':
    exe2()
