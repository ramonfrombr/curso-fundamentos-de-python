from functools import reduce  # importando o módulo reduce para usar a função reduce

lista1 = [2, 3, 4, 5, 6]

mapeando_lista1 = list(map(lambda x: x * 2, lista1))  # A FUNÇÃO MAP APLICA O COMANDO DADO A CADA ÍNDICE DE UMA LISTA
# NESTE CASO, ESTAMOS MULTIPLICANDO CADA NÚMERO DA LISTA lista1 POR 2 USANDO UMA FUNÇÃO LAMBDA

print(mapeando_lista1)

filtrando_lista1 = list(filter(lambda x: x % 2 == 0, lista1))  # A FUNÇÃO FILTER FILTRA A LISTA DE ACORDO COM NOSSA VONTADE
# NESTE CASO, ESTAMOS FILTRANDO OS NÚMEROS QUE SÃO DIVISÍVEIS POR 2 NA lista1.

print(filtrando_lista1)

def adicionar(x, y):
   return x + y
   
reduzindo_lista1 = reduce(adicionar, lista1)  # A FUNÇÃO REDUCE É USADA PARA FAZER OPERAÇÕES MATEMÁTICAS EM UMA LISTA
# AQUI, ESTAMOS SOMANDO TODOS OS NÚMEROS DA LISTA lista1

print(reduzindo_lista1)