# As strings em Python são cercadas por aspas simples ou duplas. Vamos ver a formatação de strings e alguns métodos de strings

nome = 'Ramon'
idade = 27

# Concatenar
print('Olá, meu nome é ' + nome + ' e eu tenho ' + str(idade) + ' anos')

# String Formatting

# Arguments by position
print('Meu nome é {nome} e eu tenho {idade} anos'.format(nome=nome, idade=idade))

# F-Strings (3.6+)
print(f'Olá, meu nome é {nome} e eu tenho {idade} anos.')

# String Methods

s = 'olá mundo'

# Converte primeira letra para maiúscula
print(s.capitalize())

# Converte todas para maiúsculas
print(s.upper())

# Converte todas para minúsculas
print(s.lower())

# Troca maiúsculas por minúsculas (e vice-versa)
print(s.swapcase())

# Seleciona o tamanho
print(len(s))

# Substituir
print(s.replace('mundo', 'todos'))

# Conta
sub = 'h'
print(s.count(sub))

# Começa com
print(s.startswith('olá'))

# Termina com
print(s.endswith('o'))

# Divide em uma lista
print(s.split())

# Encontra posição
print(s.find('m'))

# É alfanumérico
print(s.isalnum())

# É alfabético
print(s.isalpha())

# É numérico
print(s.isnumeric())
