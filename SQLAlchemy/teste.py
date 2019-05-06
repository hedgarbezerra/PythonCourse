import json
from SQLAlchemy.endereco import Endereco
import requests
import pprint

cep = '11080350'
url = f'http://viacep.com.br/ws/{cep}/json'
url2 = f'https://maps.googleapis.com/maps/api/js?key={apikey}'
request = requests.get(url2)
pprint.pprint(request)

"""request = request.json()
#print(request.keys())
bairro = request.get('bairro')
cep = request.get('cep')
log = request.get('logradouro')
cidade = request.get('localidade')
uf = request.get('uf')
end = Endereco(bairro, cep, log, cidade, uf)
print(end)"""
