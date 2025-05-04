# Objetivo Geral
# Aprender a converter os tipos das variáveis.

# Convertendo tipos
# Em alguns momentos é necessário e será necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:
# Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

# Inteiro para float
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2
print(preco)

# Float para inteiro
preco = 10.30
print(preco)

preco = int(preco)
print(preco)

# Conversão por divisão
preco = 10
print(preco)

print(preco / 2)

print(preco // 2)

# Numérico para string
preco = 10.50
idade = 23

print(str(preco))
print(str(idade))

texto = f'idade = {idade} e preco = {preco}'
print(texto)

# String para número
preco = '10.50'
idade = '23'

print(float(preco))
print(int(idade))

# Erro de conversão
# preco = "python"

# print(float(preco))

# Traceback (most recent call last):
# File "c:\Users\Douglas Rodrigues\Documents\GitHub\suzano_python_developer\introducao_python\conversao_de_tipos.py", line 53, in <module>
# print(float(preco))

# Exercícios

print(int(1.97348728))

print(int("10"))

print(float("10.10"))

print(float("100"))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100 / 2)

print(100 // 2)


