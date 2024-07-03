# Condições If/Else são usadas para decidir fazer algo com base em algo ser verdadeiro ou falso

x = 21
y = 20

# Operadores de Comparação (==, !=, >, <, >=, <=) - Usados para comparar valores

# If simples
if x > y:
  print(f'{x} é maior que {y}')

# If/else
if x > y:
  print(f'{x} é maior que {y}')
else:
  print(f'{y} é maior que {x}')  

# elif
if x > y:
  print(f'{x} é maior que {y}')
elif x == y:
  print(f'{x} é igual a {y}')  
else:
  print(f'{y} é maior que {x}')  

# If aninhado
if x > 2:
  if x <= 10:
    print(f'{x} é maior que 2 e menor ou igual a 10')
    

# Operadores Lógicos (and, or, not) - Usados para combinar declarações condicionais

# and
if x > 2 and x <= 10:
    print(f'{x} é maior que 2 e menor ou igual a 10')

# or
if x > 2 or x <= 10:
    print(f'{x} é maior que 2 ou menor ou igual a 10')

# not
if not(x == y):
  print(f'{x} não é igual a {y}')


# Operadores de Associação (in, not in) - Os operadores de associação são usados para testar se uma sequência está presente em um objeto

numeros = [1,2,3,4,5]

# in
if x in numeros:
  print(x in numeros)

# not in
if x not in numeros:
  print(x not in numeros)

# Operadores de Identidade (is, is not) - Comparam os objetos, não se são iguais, mas se são realmente o mesmo objeto, com a mesma localização de memória:

# is
if x is y:
  print(x is y)

# is not
if x is not y:
  print(x is not y)