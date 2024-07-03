# Um dicionário é uma coleção que é desordenada, mutável e indexada. Não há membros duplicados.

# Criar dicionário
pessoa = {
    'nome': 'João',
    'sobrenome': 'Doe',
    'idade': 30
}

# Usar o construtor
# pessoa2 = dict(nome='Sara', sobrenome='Williams')

# Obter valor
print(pessoa['nome'])
print(pessoa.get('sobrenome'))

# Adicionar chave/valor
pessoa['telefone'] = '555-555-5555'

# Obter chaves do dicionário
print(pessoa.keys())

# Obter itens do dicionário
print(pessoa.items())

# Copiar dicionário
pessoa2 = pessoa.copy()
pessoa2['cidade'] = 'Boston'

# Remover item
del(pessoa['idade'])
pessoa.pop('telefone')

# Limpar
pessoa.clear()

# Obter comprimento
print(len(pessoa2))

# Lista de dicionários
pessoas = [
    {'nome': 'Marta', 'idade': 30},
    {'nome': 'Kevin', 'idade': 25}
]

print(pessoas[1]['nome'])