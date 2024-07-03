# Uma Tupla é uma coleção ordenada e imutável. Permite membros duplicados.

# Criar tupla
frutas = ('Maçãs', 'Laranjas', 'Uvas')

# Usando um construtor
# frutas2 = tuple(('Maçãs', 'Laranjas', 'Uvas'))

# Um único valor precisa de uma vírgula final
frutas2 = ('Maçãs',)

# Obter valor
print(frutas[1])

# Não é possível mudar o valor
frutas[0] = 'Pêras'  # Isso resultará em um erro

# Excluir a tupla
del frutas2

# Obter comprimento
print(len(frutas))


# Um Conjunto é uma coleção desordenada e sem indexação. Não permite membros duplicados.

# Criar conjunto
conjunto_frutas = {'Maçãs', 'Laranjas', 'Manga'}

# Verificar se está no conjunto
print('Maçãs' in conjunto_frutas)

# Adicionar ao conjunto
conjunto_frutas.add('Uva')

# Remover do conjunto
conjunto_frutas.remove('Uva')

# Adicionar duplicado
conjunto_frutas.add('Maçãs')

# Limpar o conjunto
conjunto_frutas.clear()

# Deletar
del conjunto_frutas

print(conjunto_frutas)  # Isso resultará em um erro, pois o conjunto foi excluído