# .append()

# Adiciona um elemento ao final da lista

lista_numeros = [1, 2, 3, 4]
lista_numeros.append(5)
print(lista_numeros)  # [1, 2, 3, 4, 5]

# .copy()

# Retorna uma cópia da lista

lista_original = [10, 20, 30]
lista_copia = lista_original.copy()
lista_copia[0] = 100
print(f"Original: {lista_original}")  # [10, 20, 30]
print(f"Cópia: {lista_copia}")  # [100, 20, 30]

# .count()

# Retorna o número de ocorrências de um elemento na lista

lista_notas = [7.5, 8.0, 7.5, 9.0, 7.5]
quantidade = lista_notas.count(7.5)
print(f"A nota 7.5 aparece {quantidade} vezes")  # A nota 7.5 aparece 3 vezes

# .extend()

# Adiciona elementos de uma lista a outra

lista_pares = [2, 4, 6]
lista_impares = [1, 3, 5]
lista_pares.extend(lista_impares)
print(lista_pares)  # [2, 4, 6, 1, 3, 5]

# .index()

# Retorna o índice de um elemento na lista

lista_cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
indice = lista_cidades.index('Rio de Janeiro')
print(f"Rio de Janeiro está no índice {indice}")  # Rio de Janeiro está no índice 1

# .insert()

# Insere um elemento em uma posição específica

lista_cores = ['vermelho', 'azul', 'verde']
lista_cores.insert(1, 'amarelo')
print(lista_cores)  # ['vermelho', 'amarelo', 'azul', 'verde']

# .pop()

# Remove e retorna o último elemento da lista

lista_temperaturas = [25, 28, 30, 22]
ultima_temp = lista_temperaturas.pop()
print(f"Última temperatura: {ultima_temp}")  # Última temperatura: 22
print(f"Lista atual: {lista_temperaturas}")  # [25, 28, 30]

# .remove()

# Remove a primeira ocorrência de um elemento

lista_idades = [25, 30, 25, 35, 25]
lista_idades.remove(25)
print(lista_idades)  # [30, 25, 35, 25]

# .reverse()

# Inverte a ordem dos elementos da lista

lista_ordem = ['primeiro', 'segundo', 'terceiro', 'quarto']
lista_ordem.reverse()
print(lista_ordem)  # ['quarto', 'terceiro', 'segundo', 'primeiro']

# .sort()

# Ordena os elementos da lista

lista_precos = [10.5, 8.75, 15.25, 7.50]
lista_precos.sort()
print(lista_precos)  # [7.5, 8.75, 10.5, 15.25]

# .clear()

# Remove todos os elementos da lista

lista_tarefas = ['Estudar Python', 'Fazer exercícios', 'Revisar código']
lista_tarefas.clear()
print(lista_tarefas)  # []


# len()

# Retorna o número de elementos da lista

lista_frutas = ['banana', 'maçã', 'laranja', 'uva', 'pêra']
print(len(lista_frutas))  # 5

# sorted()

# Ordena os elementos da lista

lista_precos = [10.5, 8.75, 15.25, 7.50]
lista_precos_ordenados = sorted(lista_precos)
print(lista_precos_ordenados)  # [7.5, 8.75, 10.5, 15.25]