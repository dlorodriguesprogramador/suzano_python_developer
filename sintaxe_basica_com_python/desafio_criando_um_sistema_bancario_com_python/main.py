from datetime import datetime

menu = """
 ============== Bem Vindo ao Banco Suzano ================
 ============== Escolha uma das opções abaixo: ===========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

 Obrigado por usar nosso sistema!!!

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("O valor deve ser maior que zero!")
                continue
            return valor
        except ValueError:
            print("Por favor, digite um valor numérico válido!")

def registrar_operacao(tipo, valor):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return f"{data_hora} - {tipo}: R$ {valor:.2f}\n"

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = obter_valor("Informe o valor do depósito: ")
        saldo += valor
        extrato += registrar_operacao("Depósito", valor)
        print(f"\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===")

    elif opcao == "2":
        valor = obter_valor("Informe o valor do saque: ")

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            saldo -= valor
            extrato += registrar_operacao("Saque", valor)
            numero_saques += 1
            print(f"\n=== Saque de R$ {valor:.2f} realizado com sucesso! ===")

    elif opcao == "3":
        print("\n============== EXTRATO ==============")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print(f"Saques realizados hoje: {numero_saques}/{LIMITE_SAQUES}")
        print("========================================")

    elif opcao == "4":
        print("\nObrigado por usar o Banco Suzano! Volte sempre!")
        break

    else:
        print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")