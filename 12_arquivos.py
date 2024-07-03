# O Python possui funções para criar, ler, atualizar e excluir arquivos.

# Abrir um arquivo
meuArquivo = open('meuarquivo.txt', 'w')

# Obter algumas informações
print('Nome: ', meuArquivo.name)
print('Está Fechado: ', meuArquivo.closed)
print('Modo de Abertura: ', meuArquivo.mode)

# Escrever no arquivo
meuArquivo.write('Eu amo Python')
meuArquivo.write(' e JavaScript')
meuArquivo.close()

# Anexar ao arquivo
meuArquivo = open('meuarquivo.txt', 'a')
meuArquivo.write(' Eu também gosto de PHP')
meuArquivo.close()

# Ler do arquivo
meuArquivo = open('meuarquivo.txt', 'r+')
texto = meuArquivo.read(100)
print(texto)