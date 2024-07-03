# JSON é comumente usado com APIs de dados. Aqui está como podemos analisar JSON em um dicionário Python

import json

# JSON de exemplo
usuarioJSON = '{"nome": "João", "sobrenome": "Silva", "idade": 30}'

# Analisar para dicionário
usuario = json.loads(usuarioJSON)

# print(usuario)
# print(usuario['nome'])

carro = {'marca': 'Ford', 'modelo': 'Mustang', 'ano': 1970}

carroJSON = json.dumps(carro)

print(carroJSON)