# Parâmetros especiais

# Parâmetros especiais são parâmetros que podem ser usados para definir o comportamento de uma função.

# Positional-only parameters (/)

# Positional-only parameters são parâmetros que podem ser usados para definir o comportamento de uma função.

def multiplicacao(a, b, /):  # Parâmetros posicionais apenas
    return a * b

print(multiplicacao(2, 3))  # Funciona
# print(multiplicacao(a=2, b=3))  # Isso geraria erro

# Keyword-only parameters (*)

# Keyword-only parameters são parâmetros que podem ser usados para definir o comportamento de uma função.

def potencia(*, base, expoente):  # Parâmetros nomeados apenas
    return base ** expoente

print(potencia(base=2, expoente=3))  # Funciona
# print(potencia(2, 3))  # Isso geraria erro

# Keyword-only and positional-only parameters

# Keyword-only and positional-only parameters são parâmetros que podem ser usados para definir o comportamento de uma função.

def calculadora(x, y, /, *, operacao):  # Mistura de parâmetros posicionais e nomeados
    if operacao == 'soma':
        return x + y
    elif operacao == 'subtracao':
        return x - y
    return None

print(calculadora(10, 5, operacao='soma'))

# Objetivos de primeira classe

# Objetivos de primeira classe são objetos que podem ser passados como argumentos para outras funções, retornados como resultado de uma função e armazenados em variáveis.

def aplicar_operacao(func, a, b):
    return func(a, b)

def soma(a, b):
    return a + b

print(aplicar_operacao(soma, 5, 3))  # Passando função como argumento

# Escopo local e escopo global

# Escopo local é o escopo onde a variável é definida.
# Escopo global é o escopo onde a variável é definida.

contador = 0  # Variável global

def incrementar():
    global contador  # Declarando que vamos usar a variável global
    contador += 1
    return contador

print(incrementar())  # Incrementa e retorna 1
print(incrementar())  # Incrementa e retorna 2