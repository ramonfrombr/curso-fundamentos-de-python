# Um módulo é basicamente um arquivo contendo um conjunto de funções para incluir em sua aplicação. Existem módulos principais do Python, módulos que você pode instalar usando o gerenciador de pacotes pip (incluindo o Django) e também módulos personalizados.

# Módulos principais
import datetime
from datetime import date
import time
from time import time

# Módulo do pip
from camelcase import CamelCase

# Importar módulo personalizado
import validador
from validador import validar_email

# hoje = datetime.date.today()
hoje = date.today()
timestamp = time()

c = CamelCase()
# print(c.hump('olá mundo'))

email = 'teste#teste.com'
if validar_email(email):
    print('O email é válido')
else:
    print('O email é inválido')