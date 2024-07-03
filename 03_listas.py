# Uma lista é uma coleção que é ordenada e alterável. Permite valores duplicados.

# Criar lista
numeros = [1, 2, 3, 4, 5]
frutas = ['Maçãs', 'Laranjas', 'Bananas', 'Peras']

# Usando um construtor
# numeros2 = list((1, 2, 3, 4, 5))

# Selecionar um valor
print(frutas[1])

# Selecionar o último valor
print(frutas[-1])

# Selecionar o tamanho
print(len(frutas))

# Adicionar à lista
frutas.append('Mangas')

# Remover da lista
frutas.remove('Uvas')

# Inserir em determinada posição
frutas.insert(2, 'Morangos')

# Alterar valor de um elemento
frutas[0] = 'Melancias'

# Remover de determinada posição
frutas.pop(2)

# Reverter lista
frutas.reverse()

# Ordenar lista
frutas.sort()

# Ordenar lista ao reverso
frutas.sort(reverse=True)

print(frutas)
