class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


class SistemaBancario:
    def __init__(self):
        self.contas = []


    def criar_conta(self, titular, saldo):
        nova_conta = ContaBancaria(titular, saldo)
        self.contas.append(nova_conta)


    def listar_contas(self):
        dados_contas = []  # Lista para armazenar os dados de cada conta formatados
        for conta in self.contas:
            dados_contas.append(f"{conta.titular}: R$ {conta.saldo}")
        print(", ".join(dados_contas))  # Imprime todos os dados formatados em uma única linha


sistema = SistemaBancario()


while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))


sistema.listar_contas()