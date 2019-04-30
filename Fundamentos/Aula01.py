from Fundamentos.User import User

user1 = User('Hedgar', 22, 1.70)
user2 = User('Amanda', 11, 1.55)
user_list = []
mais = 1
while mais !=0:
    try:
        nome = str(input('Insira seu nome: \n'))
        idade = int(input('Insira sua idade: \n'))
        altura = float(input('Insira sua altura: \n'))
        user = User(nome, idade, altura)
        user_list.append(user)
        mais = int(input('Deseja continuar? 1 - Sim 0 - Não \n'))

    except ValueError:
        print('Tipo de dado inválido! \n')
for user in user_list:
    user.data()
