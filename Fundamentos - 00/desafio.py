saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3


def depositar():
    valor = float(input("Depositar: R$ "))
    if valor > 0:
        global saldo , extrato
        saldo  = saldo + valor
        extrato += f"Depósito: RS {valor:.2f}\n"
    else:
        print("valor inválido")


def sacar():
    global LIMITES_SAQUES, saldo, extrato
    valor = float(input("Sacar: R$ "))


    if valor > 0 and valor <= saldo:
        if LIMITES_SAQUES > 0:
            if valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                LIMITES_SAQUES -= 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print(f"O valor do saque excede o limite permitido de R$ {limite:.2f}.")
        else:
            print("Limite de saques diário atingido.")
    else:
        print("Saldo insuficiente ou valor inválido")

def mostrar_extrato():
    global saldo, extrato
    print("\n======= EXTRATO =======")
    print("Nenhuma movimentação." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=======================")


def exibir_menu():
    print("""
                        BEM VINDO AO BANCO

                        [1] - Depositar
                        [2] - Sacar
                        [3] - Extrato
                        [4] - Sair
    """)


while True:
    exibir_menu()  #
    opcao = int(input("Escolha uma opção"))

    if opcao == 1:
        depositar()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        mostrar_extrato()
    elif opcao == 4:
        break

