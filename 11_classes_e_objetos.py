# Uma classe é como uma planta para criar objetos. Um objeto tem propriedades e métodos (funções) associadas a ele. Quase tudo em Python é um objeto.

# Criar classe
class Usuario:

    # Construtor
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        
        # Adicionando Encapsulamento de variáveis... Encapsulamento é o conceito de tornar as variáveis não acessíveis ou acessíveis até certo ponto pelas classes filhas
        self._privado = 1000 # As variáveis encapsuladas são declaradas com '_' no construtor.

    def saudacao(self):
        return f'Meu nome é {self.nome} e eu tenho {self.idade} anos'

    def aniversario(self):
        self.idade += 1
    
    # função para variável encapsulada
    def imprimir_encapsulado(self):
        print(self._privado)

# Estender classe
class Cliente(Usuario):
    # Construtor
    def __init__(self, nome, email, idade):
        Usuario.__init__(self, nome, email, idade) # Chama o construtor adequado da classe pai para torná-lo como uma classe filha adequada herdando todos os métodos.
        self.nome = nome
        self.email = email
        self.idade = idade
        self.saldo = 0

    def definir_saldo(self, saldo):
        self.saldo = saldo

    def saudacao(self):
        return f'Meu nome é {self.nome} e eu tenho {self.idade} anos e meu saldo é {self.saldo}'

# Iniciar objeto de usuário
brad = Usuario('Brad Traversy', 'brad@gmail.com', 37)
# Iniciar objeto de cliente
janet = Cliente('Janet Johnson', 'janet@yahoo.com', 25)

janet.definir_saldo(500)
print(janet.saudacao())

brad.aniversario()
print(brad.saudacao())

# Encapsulamento -->
brad.imprimir_encapsulado()
brad._privado = 800 # Mudando para brad
brad.imprimir_encapsulado()

# Método herdado do pai
janet.imprimir_encapsulado() # Mudar a variável para brad não afeta a variável de janet --> Encapsulamento
janet._privado = 600
janet.imprimir_encapsulado()

# Da mesma forma, mudar para janet não afeta a variável de brad.
brad.imprimir_encapsulado()