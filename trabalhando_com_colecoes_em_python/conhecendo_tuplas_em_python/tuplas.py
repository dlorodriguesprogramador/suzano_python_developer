# Criando tuplas

# Tuplas são sequências imutáveis de objetos. Podem ser criadas usando parênteses () ou a função tuple().

# Exemplo 1: Criando uma tupla com parênteses

tupla_frutas = ('banana', 'maçã', 'laranja')

# Exemplo 2: Criando uma tupla com a função tuple()

tupla_numeros = tuple(range(10))

# Acesso aos dados

print(tupla_frutas[0]) # banana
print(tupla_frutas[1]) # maçã

# Tuplas aninhadas

tupla_matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(tupla_matriz[0]) # (1, 2, 3)
print(tupla_matriz[1][2]) # 6

# Fatiamento

print(tupla_frutas[1:3]) # ('maçã', 'laranja')
print(tupla_frutas[:2]) # ('banana', 'maçã')
print(tupla_frutas[2:]) # ('laranja',)

# .count()

print(tupla_frutas.count('banana')) # 1

# .index()

print(tupla_frutas.index('maçã')) # 1

# len()

print(len(tupla_frutas)) # 3
