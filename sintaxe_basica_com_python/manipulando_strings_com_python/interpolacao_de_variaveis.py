# Introdução

# Em python temos 3 formas de interpolar variáveis em strings, 
# a primeira é usando o sinal de porcentagem (%), a segunda é usando o método format e a terceira é usando f-strings.

# A primeira forma é a mais antiga e a menos conveniente.

# Old styles %

nome = 'Guilherme'

print('Nome: %s' % nome)

# Método format

print('Nome: {}'.format(nome))

# f-strings

print(f'Nome: {nome}')

# Formatar strings com f-strings

valor = 123456.789

print(f'R$ {valor:,.2f}')