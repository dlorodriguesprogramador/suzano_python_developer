# O que são funçoes?

# Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. 
# Usar funções torna o código mais legível e possibilidade o reaproveitamento de código. 
# Programar baseado em funções, é o mesmo que dizer que estamos programando de forma estruturada.

# Exemplo de função:

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("João"))

# Retornando um valorores:

# Para retornar um valor, utilizamos a palavra reservada return. Toda a função Python retorna None por padrão.
# Diferente de outras linguagens de programação, em Python podemos retornar mais de um valor de uma função.

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("João"))

# Argumentos

# Argumentos são os valores passados para a função.

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("João"))

# Args e Kwargs

# Args e Kwargs são argumentos não nomeados e argumentos nomeados, respectivamente.

def saudacao(nome, sobrenome):
    return f"Olá, {nome} {sobrenome}!"

print(saudacao("João", "Silva"))

# Args

# Args é um argumento não nomeado.

def saudacao(*args):
    return f"Olá, {args[0]} {args[1]}!"

print(saudacao("João", "Silva"))

# Kwargs

# Kwargs é um argumento nomeado.

def saudacao(**kwargs):
    return f"Olá, {kwargs['nome']} {kwargs['sobrenome']}!"

print(saudacao(nome="João", sobrenome="Silva"))