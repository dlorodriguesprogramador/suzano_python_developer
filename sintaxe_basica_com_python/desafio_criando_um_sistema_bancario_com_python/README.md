# Sistema Bancário em Python

## Descrição
Este é um sistema bancário simples desenvolvido em Python que permite realizar as operações básicas de uma conta bancária: depósito, saque e visualização de extrato. O sistema foi desenvolvido como parte de um desafio de programação.

## Funcionalidades
- [x] Depositar
  - Aceita apenas valores positivos
  - Exibe mensagem de sucesso
  - Registra data e hora da operação

- [x] Sacar
  - Limite de 3 saques diários
  - Limite máximo de R$ 500,00 por saque
  - Verifica saldo suficiente
  - Exibe mensagem de sucesso
  - Registra data e hora da operação

- [x] Extrato
  - Lista todas as operações realizadas
  - Mostra data e hora de cada operação
  - Exibe saldo atual
  - Mostra quantidade de saques realizados no dia
  - Formato: R$ xxx.xx

## Requisitos
- Python 3.x

## Como Executar
1. Clone o repositório
2. Navegue até o diretório do projeto
3. Execute o arquivo principal:
```bash
python main.py
```

## Estrutura do Projeto
```
desafio_criando_um_sistema_bancario_com_python/
│
├── main.py
└── README.md
```

## Regras de Negócio
- Limite de 3 saques diários
- Limite máximo de R$ 500,00 por saque
- Não é possível sacar mais que o saldo disponível
- Todos os valores são exibidos no formato R$ xxx.xx
- O extrato mostra todas as operações realizadas com data e hora

## Melhorias Implementadas
- Tratamento de erros para entradas inválidas
- Formatação de data e hora nas operações
- Mensagens de sucesso e erro mais claras
- Interface mais amigável e intuitiva
- Validação de valores negativos ou zero

## Licença
Este projeto está sob a licença MIT.
