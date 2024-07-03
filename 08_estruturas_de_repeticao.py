# Um loop for é usado para iterar sobre uma sequência (que pode ser uma lista, uma tupla, um dicionário, um conjunto ou uma string).

pessoas = ['João', 'Paulo', 'Sara', 'Susana']

# Loop for simples
for pessoa in pessoas:
    print(f'Pessoa Atual: {pessoa}')

# Break
for pessoa in pessoas:
    if pessoa == 'Sara':
        break
    print(f'Pessoa Atual: {pessoa}')

# Continue
for pessoa in pessoas:
    if pessoa == 'Sara':
        continue
    print(f'Pessoa Atual: {pessoa}')

# range
for i in range(len(pessoas)):
    print(pessoas[i])

for i in range(0, 11):
    print(f'Número: {i}')

# Os loops while executam um conjunto de instruções enquanto uma condição for verdadeira.
contador = 0
while contador < 10:
    print(f'Contagem: {contador}')
    contador += 1