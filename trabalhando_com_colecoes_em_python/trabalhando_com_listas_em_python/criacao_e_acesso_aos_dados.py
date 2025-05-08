# Criando listas

# Listas em python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar uma lista usando colchetes [] ou a função list().


# Exemplo 1: Criando uma lista com colchetes

lista_frutas = ['banana', 'maçã', 'laranja', 'uva']

# Exemplo 2: Criando uma lista com a função list()

lista_numeros = list(range(10))

# Acesso direto aos dados

print(lista_frutas[0]) # banana
print(lista_frutas[3]) # uva

# Listas aninhadas

lista_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista_matriz[0]) # [1, 2, 3]
print(lista_matriz[1][2]) # 6

# Fatiamento

print(lista_frutas[1:3]) # ['maçã', 'laranja']
print(lista_frutas[:2]) # ['banana', 'maçã']
print(lista_frutas[2:]) # ['laranja', 'uva']

# Compreensão de listas

quadrados = [x**2 for x in range(10)]
print(quadrados) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtro versão 1

pares = [x for x in range(10) if x % 2 == 0]
print(pares) # [0, 2, 4, 6, 8]

# Filtro versão 2

def eh_par(x):
    return x % 2 == 0

pares = list(filter(eh_par, range(10)))
print(pares) # [0, 2, 4, 6, 8]

# Modificando valores versão 1

quadrados = [x**2 for x in range(10)]
print(quadrados) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Modificando valores versão 2

quadrados = []
for x in range(10):
    quadrados.append(x**2)
print(quadrados) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
