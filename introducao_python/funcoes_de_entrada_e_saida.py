# Função input

# A função builtin input é utlizada quando queremos ler dados da entrada padrão (teclado). 
# Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). 
# A função lê a entrada, converte para string e retorna o valor.

# Exemplo: 
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Função print

# A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). 
# Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file, flush). 
# Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

# Exemplo: 
nome = "João"
sobrenome = "Silva"
print(nome, sobrenome)
print(nome, sobrenome, sep="#")
print(nome, sobrenome, end="...\n")

# Exercício:

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"Nome: {nome}")
print(f"Idade: {idade}")

print("Nome: ", nome, "Idade: ", idade)

print("Nome: ", nome, "Idade: ", idade, sep="#")

print("Nome: ", nome, "Idade: ", idade, end="...\n")

print("Nome: ", nome, "Idade: ", idade, end="...\n", sep="#")
