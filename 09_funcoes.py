# Uma função é um bloco de código que só é executado quando é chamado. Em Python, não precisamos usar chaves, nós usamos identação com tab ou espaços.

# Criar função
def cumprimentar(nome='Fulano'):
    print(f'Olá {nome}')

# Retornar valores
def somar(numero1, numero2):
    total = numero1 + numero2
    return total

# Uma função lambda é uam função anônima pequena
# Uma função lambda pode receber qualquer número de argumentos, mas só pode ter uma expressão.
multiplicar = lambda numero1, numero2: numero1 * numero2

print(somar(10, 3))
