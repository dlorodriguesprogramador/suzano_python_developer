# Métodos da classe dict

# .clear()

# Remove todos os pares chave-valor do dicionário

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Usando o método clear() para limpar o dicionário
produto.clear()

# Saída: {}

# .copy()

# Retorna uma cópia superficial do dicionário

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Usando o método copy() para criar uma cópia do dicionário
produto_copia = produto.copy()

# Saída: {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# .fromkeys()

# Cria um novo dicionário com as chaves fornecidas e valores padrão

# Criando um dicionário com chaves e valores padrão
chaves = ['produto', 'quantidade', 'preco']
valores = ['Smartphone', 5, 2000.00]

# Usando o método fromkeys() para criar um novo dicionário
novo_dicionario = dict.fromkeys(chaves, valores)

# Saída: {'produto': ['Smartphone', 5, 2000.00], 'quantidade': ['Smartphone', 5, 2000.00], 'preco': ['Smartphone', 5, 2000.00]}

# .get()

# Obtém o valor associado a uma chave, com um valor padrão se a chave não existir

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Usando o método get() para obter o valor associado a uma chave
valor = produto.get('preco')

# Saída: 3500.00

# .items()

# Retorna um objeto de visualização que mostra os pares chave-valor do dicionário

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Usando o método items() para obter os pares chave-valor do dicionário
pares = produto.items()

# Saída: dict_items([('nome', 'Notebook'), ('preco', 3500.00), ('marca', 'Dell')])

# .keys()

# Retorna um objeto de visualização que mostra as chaves do dicionário

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Usando o método keys() para obter as chaves do dicionário
chaves = produto.keys()

# Saída: dict_keys(['nome', 'preco', 'marca'])

# .pop()

# Remove e retorna o valor associado a uma chave específica

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Usando o método pop() para remover e obter o valor associado a uma chave
valor = produto.pop('preco')

# Saída: 3500.00

# Saída: {'nome': 'Notebook', 'marca': 'Dell'}

# .popitem()

# Remove e retorna o último par chave-valor do dicionário

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Usando o método popitem() para remover e obter o último par chave-valor
ultimo_par = produto.popitem()

# Saída: ('marca', 'Dell')

# Saída: {'nome': 'Notebook', 'preco': 3500.00}

# .setdefault()

# Obtém o valor associado a uma chave, criando-o se não existir

# Criando um dicionário
produto = {'nome': 'Notebook', 'marca': 'Dell'}

# Usando o método setdefault() para obter o valor associado a uma chave
valor = produto.setdefault('preco', 3500.00)

# Saída: 3500.00

# Saída: {'nome': 'Notebook', 'marca': 'Dell', 'preco': 3500.00}

# .update()

# Atualiza o dicionário com pares chave-valor de outro dicionário

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Criando outro dicionário
produto2 = {'preco': 3800.00, 'garantia': '12 meses'}

# Usando o método update() para atualizar o dicionário
produto.update(produto2)

# Saída: {'nome': 'Notebook', 'preco': 3800.00, 'marca': 'Dell', 'garantia': '12 meses'}

# .values()

# Retorna um objeto de visualização que mostra os valores do dicionário

# Criando um dicionário
produto = {'nome': 'Notebook', 'preco': 3500.00, 'marca': 'Dell'}

# Usando o método values() para obter os valores do dicionário
valores = produto.values()

# Saída: dict_values(['Notebook', 3500.00, 'Dell'])