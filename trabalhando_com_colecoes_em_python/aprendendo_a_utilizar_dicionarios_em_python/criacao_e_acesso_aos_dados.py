# Criando um dicionário

# Um dicionário é uma coleção de pares chave-valor.
# As chaves são únicas e imutáveis, enquanto os valores podem ser de qualquer tipo.

# Criando um dicionário

# Criando um dicionário com pares chave-valor
pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Acessando um valor pela chave
print(pessoa['nome'])  # Saída: João

# Adicionando um novo par chave-valor
pessoa['profissao'] = 'Engenheiro'
print(pessoa)  # Saída: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# Modificando um valor existente
pessoa['idade'] = 31
print(pessoa)  # Saída: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# Removendo um par chave-valor
del pessoa['cidade']
print(pessoa)  # Saída: {'nome': 'João', 'idade': 31, 'profissao': 'Engenheiro'}

# Verificando se uma chave existe
print('cidade' in pessoa)  # Saída: False
print('profissao' in pessoa)  # Saída: True

# Iterando sobre um dicionário
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

# Dicionários aninhados

# Criando um dicionário com dicionários
pessoas = {
    'pessoa1': {'nome': 'João', 'idade': 30},
    'pessoa2': {'nome': 'Maria', 'idade': 25}
}

# Iterar dicionários aninhados
for pessoa_id, info in pessoas.items():
    print(f'{pessoa_id}: {info}')