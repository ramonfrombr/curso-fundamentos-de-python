# Uma variável é um contêiner para um valor, que pode ser de vários tipos

'''
Este é um
comentário de várias linhas
ou docstring (usada para definir o propósito de uma função)
pode ser aspas simples ou duplas
'''

"""
REGRAS DAS VARIÁVEIS:
  - Os nomes das variáveis são sensíveis a maiúsculas e minúsculas (nome e NOME são variáveis diferentes)
  - Deve começar com uma letra ou um sublinhado
  - Pode ter números, mas não pode começar com um
"""

x = 1
y = 2.5
nome = "Pedro"
confirmado = True

# Múltipla atribuição
x, y, nome, confirmado = (1, 2.5, 'Pedro', True)

# Matemática básica
a = x + y

# Conversão de tipo
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)
