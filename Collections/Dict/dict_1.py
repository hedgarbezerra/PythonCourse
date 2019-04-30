my_dict = {1: 'Hedgar', 2: 'Matheus', 3: 'Arthur'}
dict_2 = dict({'nome': ['Hedgar', 'Matheus', 'Arthur'], 'sobrenome': 'Bezerra'})
json = dict({'id': 1, 'nome': 'Hedgar', 'sobrenome': 'Bezerra', 'lat': 2332.221119, 'long': 83.114343,
             'telefone': '13-991931364'})

for chave, valor in my_dict.items():
    print(chave, valor)

print(dict_2.get('nome'))
print(json.items())

for chave, valor in json.items():
    print(chave, valor)

latlng = str(json.get('lat')) + '  ' + str(json.get('long'))
print(latlng)

"""Keys mostra as chaves"""
print(json.keys())

"""Adicionar no dicionário e criar nova chave"""
json['email'] = 'hesydqu@gmail.com'
print(json)

"""Metodo clear limpa todos elementos"""
json.clear()
print(json)