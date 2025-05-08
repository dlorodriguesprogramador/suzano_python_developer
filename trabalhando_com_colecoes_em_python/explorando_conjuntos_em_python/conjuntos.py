# Criando sets

# Sets são coleções não ordenadas e não indexadas. Podem ser criados usando chaves {} ou a função set().

# Exemplo 1: Criando um set com chaves
conjunto_cidades = {'São Paulo', 'Rio de Janeiro', 'Belo Horizonte'}

# Exemplo 2: Criando um set com a função set()
conjunto_idades = set([25, 30, 35, 40, 45])

# Acesso aos dados
print(conjunto_cidades)  # {'São Paulo', 'Rio de Janeiro', 'Belo Horizonte'}
print(conjunto_idades)  # {25, 30, 35, 40, 45}

# Função enumerate()
print("\nListando cidades:")
for i, cidade in enumerate(conjunto_cidades, 1):
    print(f"Cidade {i}: {cidade}")

# .union()
conjunto_cidades_2 = {'Salvador', 'Recife', 'Belo Horizonte'}
conjunto_cidades_unidas = conjunto_cidades.union(conjunto_cidades_2)
print("\nUnião de cidades:", conjunto_cidades_unidas)

# .intersection()
conjunto_idades_2 = {30, 35, 40, 45, 50}
conjunto_idades_comuns = conjunto_idades.intersection(conjunto_idades_2)
print("\nIdades em comum:", conjunto_idades_comuns)

# .difference()
conjunto_cores_1 = {'vermelho', 'azul', 'verde'}
conjunto_cores_2 = {'azul', 'amarelo', 'verde'}
conjunto_cores_diferenca = conjunto_cores_1.difference(conjunto_cores_2)
print("\nCores únicas no primeiro conjunto:", conjunto_cores_diferenca)

# .symmetric_difference()
conjunto_numeros_1 = {1, 2, 3, 4, 5}
conjunto_numeros_2 = {4, 5, 6, 7, 8}
conjunto_numeros_diferenca_simetrica = conjunto_numeros_1.symmetric_difference(conjunto_numeros_2)
print("\nNúmeros que não se repetem:", conjunto_numeros_diferenca_simetrica)

# .issubset()
conjunto_vogais = {'a', 'e', 'i'}
conjunto_alfabeto = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
print("\nVogais são subconjunto do alfabeto:", conjunto_vogais.issubset(conjunto_alfabeto))

# .issuperset()
conjunto_pares = {2, 4, 6, 8, 10}
conjunto_numeros = {2, 4, 6}
print("\nConjunto de pares contém os números:", conjunto_pares.issuperset(conjunto_numeros))

# .isdisjoint()
conjunto_impares = {1, 3, 5, 7}
conjunto_pares = {2, 4, 6, 8}
print("\nConjuntos são disjuntos:", conjunto_impares.isdisjoint(conjunto_pares))

# .add()
conjunto_temperaturas = {25, 28, 30}
conjunto_temperaturas.add(32)
print("\nTemperaturas após adicionar:", conjunto_temperaturas)

# .clear()
conjunto_tarefas = {'Estudar', 'Trabalhar', 'Exercitar'}
conjunto_tarefas.clear()
print("\nConjunto de tarefas após limpar:", conjunto_tarefas)

# .copy()
conjunto_original = {'Python', 'Java', 'JavaScript'}
conjunto_copia = conjunto_original.copy()
conjunto_copia.add('C++')
print("\nOriginal:", conjunto_original)
print("Cópia:", conjunto_copia)

# .discard()
conjunto_notas = {7.5, 8.0, 9.0}
conjunto_notas.discard(8.0)
print("\nNotas após descartar:", conjunto_notas)

# .pop()
conjunto_cores = {'vermelho', 'azul', 'verde', 'amarelo'}
cor_removida = conjunto_cores.pop()
print("\nCor removida:", cor_removida)
print("Cores restantes:", conjunto_cores)

# .remove()
conjunto_frutas = {'maçã', 'banana', 'laranja'}
conjunto_frutas.remove('banana')
print("\nFrutas após remover:", conjunto_frutas)

# len()
conjunto_estados = {'SP', 'RJ', 'MG', 'BA', 'PE'}
print("\nNúmero de estados:", len(conjunto_estados))

# in
conjunto_meses = {'Janeiro', 'Fevereiro', 'Março'}
print("\n'Março' está no conjunto:", 'Março' in conjunto_meses)
print("'Abril' está no conjunto:", 'Abril' in conjunto_meses)
