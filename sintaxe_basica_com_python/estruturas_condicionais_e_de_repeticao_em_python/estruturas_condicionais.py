# Estruturas condicionais

# A estrutura condicional mais comum é o if.

# Exemplo:

x = int(input("Digite um número para x: "))

if x > 10:
    print("x é maior que 10")   

# O if é uma estrutura condicional que executa um bloco de código se uma condição for verdadeira.

# else

# O else é uma estrutura condicional que executa um bloco de código se uma condição for falsa.

# Exemplo:

if x > 10:
    print("x é maior que 10")
else:
    print("x é menor que 10")

# elif

# O elif é uma estrutura condicional que executa um bloco de código se uma condição for verdadeira.

# Exemplo:

if x > 10:
    print("x é maior que 10")
elif x == 10:
    print("x é igual a 10")
else:
    print("x é menor que 10")

# Exercício:

# Crie um programa que receba um número e imprima se ele é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
