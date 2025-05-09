import textwrap
from datetime import datetime
from typing import List, Dict, Union, Optional


def menu() -> str:
    menu = """\n
    ====== Bem Vindo ao Banco Suzano ==========
    ====== Escolha uma das opções abaixo: =====
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    Obrigado por usar nosso sistema!!!
    ==>  """
    return input(textwrap.dedent(menu))


def obter_valor(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("\n@@@ O valor deve ser maior que zero! @@@")
                continue
            return valor
        except ValueError:
            print("\n@@@ Por favor, digite um valor numérico válido! @@@")


def depositar(saldo: float, valor: float, extrato: str, /) -> tuple[float, str]:
    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{data_hora} - Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo: float, valor: float, extrato: str, limite: float, 
          numero_saques: int, limite_saques: int) -> tuple[float, str, int]:
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{data_hora} - Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato, numero_saques


def exibir_extrato(saldo: float, /, *, extrato: str) -> None:
    print("\n============ EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===================================")


def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if int(cpf[9]) != digito1:
        return False
    
    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if int(cpf[10]) != digito2:
        return False
    
    return True


def validar_data_nascimento(data: str) -> bool:
    try:
        dia, mes, ano = map(int, data.split('-'))
        if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2024):
            return False
        return True
    except:
        return False


def criar_usuario(usuarios: List[Dict]) -> None:
    print("\n=== Cadastro de Novo Usuário ===")
    cpf = input("Informe o CPF (somente número): ")
    
    if not validar_cpf(cpf):
        print("\n@@@ CPF inválido! @@@")
        return

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ").strip()
    if not nome:
        print("\n@@@ Nome não pode estar vazio! @@@")
        return

    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    if not validar_data_nascimento(data_nascimento):
        print("\n@@@ Data de nascimento inválida! Use o formato dd-mm-aaaa @@@")
        return

    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
    if not endereco:
        print("\n@@@ Endereço não pode estar vazio! @@@")
        return

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\n=== Usuário criado com sucesso! ===")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")


def criar_conta(agencia: str, numero_conta: int, usuarios: List[Dict]) -> Optional[Dict]:
    print("\n=== Criação de Nova Conta ===")
    if not usuarios:
        print("\n@@@ Não existem usuários cadastrados! Cadastre um usuário primeiro. @@@")
        return None

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        print(f"Agência: {agencia}")
        print(f"Conta: {numero_conta}")
        print(f"Titular: {usuario['nome']}")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0.0,
            "extrato": "",
            "numero_saques": 0
        }
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None


def filtrar_usuario(cpf: str, usuarios: List[Dict]) -> Optional[Dict]:
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas: List[Dict]) -> None:
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada! @@@")
        return

    print("\n=== Lista de Contas Cadastradas ===")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            CPF:\t\t{conta['usuario']['cpf']}
            Saldo:\t\tR$ {conta.get('saldo', 0.0):.2f}
            Endereço:\t{conta['usuario']['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main() -> None:
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            if not contas:
                print("\n@@@ Não existem contas cadastradas! Crie uma conta primeiro. @@@")
                continue
            valor = obter_valor("Informe o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            if not contas:
                print("\n@@@ Não existem contas cadastradas! Crie uma conta primeiro. @@@")
                continue
            valor = obter_valor("Informe o valor do saque: ")
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            if not contas:
                print("\n@@@ Não existem contas cadastradas! Crie uma conta primeiro. @@@")
                continue
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)           
        
        elif opcao == "nc":
            if not usuarios:
                print("\n@@@ Não existem usuários cadastrados! Cadastre um usuário primeiro. @@@")
                continue
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por usar o Banco Suzano! Volte sempre!")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()
