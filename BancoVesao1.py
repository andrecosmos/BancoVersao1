apresentacao = """
**************************************************
            Bem-vindo ao Banco QUEBRADO!
**************************************************
"""
print(apresentacao)

menu = """
------------------------------------------------
         Operações disponíveis:

1. Depositar
2. Sacar
3. Extrato

-------------------------------------------------
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
continuar = True

while (continuar != "n"):

    print(menu)
    opcao = input("\nDigite a operação desejada: ")

    if opcao == "1":
        valor = float(input("\nDigite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\nValor inválido para depósito.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if valor > saldo:
            print("\nSaldo insuficiente.")
        elif valor > limite:
            print("\nValor acima do limite permitido.")
        elif numero_saques >= LIMITE_SAQUES:
            print("\nNúmero máximo de saques atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "3":
        print("\n==================== Extrato ====================")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"\n Saques realizados :  {numero_saques} de {LIMITE_SAQUES} ")
        print("=================================================")


    else:
        print("Opção inválida. Tente novamente.")
    continuar = input("Deseja continuar? (s/n): ").lower()