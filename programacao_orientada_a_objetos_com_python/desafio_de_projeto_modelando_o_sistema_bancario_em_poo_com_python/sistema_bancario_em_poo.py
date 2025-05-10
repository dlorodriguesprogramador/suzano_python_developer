import textwrap
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            conta.realizar_transacao(transacao)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False

    def realizar_transacao(self, transacao):
        transacao.registrar(self)

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        saques = [t for t in self._historico.transacoes if t["tipo"] == "Saque"]
        if len(saques) >= self._limite_saques:
            erro("Limite de saques atingido.")
            return False
        elif valor > self._limite:
            erro("O valor do saque excede o limite permitido.")
            return False
        return super().sacar(valor)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar(self)

# Funções auxiliares
def erro(msg):
    print(f"\n@@@ {msg} @@@")

def menu():
    menu_texto = """
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu_texto)).strip().lower()

def filtrar_cliente(clientes, cpf):
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            return cliente
    return None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        erro("Cliente não possui conta!")
        return None
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(clientes, cpf)

    if not cliente:
        erro("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        erro("Valor inválido.")
        return

    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(clientes, cpf)

    if not cliente:
        erro("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        erro("Valor inválido.")
        return

    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(clientes, cpf)

    if not cliente:
        erro("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    transacoes = conta.historico.transacoes
    extrato = "\n".join(
        f"{t['tipo']}:\n\tR$ {t['valor']:.2f}" for t in transacoes
    ) if transacoes else "Não foram realizadas movimentações."

    print("\n========== EXTRATO ==========")
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==============================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_cliente(clientes, cpf):
        erro("Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/estado): ")

    cliente = PessoaFisica(nome=nome, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(clientes, cpf)

    if not cliente:
        erro("Cliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente(numero=numero, cliente=cliente)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 20)
        print(f"Agência: {conta.agencia}")
        print(f"C/C: {conta.numero}")
        print(f"Titular: {conta.cliente.nome}")

# Execução principal
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero = len(contas) + 1
            criar_conta(numero, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            erro("Operação inválida. Por favor, selecione novamente.")

if __name__ == "__main__":
    main()
