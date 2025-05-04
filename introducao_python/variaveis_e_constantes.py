# Variaveis

# Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa.
# Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem premanecer com o mesmo 
# durante toda a execução do programa.

# age = 23
# name = "John"
# print(f'Meu nome é {name} e tenho {age} ano(s) de idade.')
# >>> Meu nome é John e tenho 23 ano(s) de idade.

# age, name = (23, "John")
# print(f'Meu nome é {name} e tenho {age} ano(s) de idade.')
# >>> Meu nome é John e tenho 23 ano(s) de idade.

# Alterando os valores

# Perceba que não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente para nós. 
# Por isso não podemos simplismente criar uma variável sem atribuir um valor. 
# Para alterar o valor da variável basta fazer uma atribuição de um novo valor.

# age = 23
# name = "John"
# print(f'Meu nome é {name} e tenho {age} ano(s) de idade.')
# >>> Meu nome é John e tenho 23 ano(s) de idade.

# age = 24
# name = "Jane"
# print(f'Meu nome é {name} e tenho {age} ano(s) de idade.')
# >>> Meu nome é Jane e tenho 24 ano(s) de idade.

# Constantes

# Assim como as variáveis, constantes são utilizadas para armazenar valores. 
# Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja o valor é imutável.

# age = 23
# name = "John"
# print(f'Meu nome é {name} e tenho {age} ano(s) de idade.')
# >>> Meu nome é John e tenho 23 ano(s) de idade.

# age = 24
# name = "Jane"
# print(f'Meu nome é {name} e tenho {age} ano(s) de idade.')
# >>> Meu nome é Jane e tenho 24 ano(s) de idade.

# Python não tem constantes

# Não existe uma palavra reservada para informar ao interpretador que o valor é constante. 
# Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.
# Em python usamos a convenção que diz ao programador que a variável é uma constante. 
# Para fazer isso, você deve criar a variável com o nome todo em letras maíusculas:

# ABS_PATH = '/home/user/python'
# DEBUG = True
# STATE = [
#     'SP',
#     'RJ',
#     'MG'
# ]
# AMOUNT = 30.2

# Boas práticas
# O padrão de nomes deve ser snake case.
# Escolher nomes sugestivos.
# Nome de constantes todo em maiúsculo.

nome = "John"
idade = 23

nome, idade = "Jane", 24

print(f'Meu nome é {nome} e tenho {idade} ano(s) de idade.')

limite_saque_diario = 1000

BRAZILIAN_STATES = [
    'SP',
    'RJ',
    'MG'
]

print(BRAZILIAN_STATES)









