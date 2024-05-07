saldo = 0
numero_saques = 0
limite = 500
LIMITE_SAQUES = 3
extrato = ""

while True:

    menu = input('\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n') 

    if menu == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha ao realizar depósito, TRente novamente")

    elif menu == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo :
            print("Falha na operação! saldo insuficiente.")

        elif  valor > limite:
            print("Falha na operação! valor acima do limite para saque.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Falha na operação! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("FAlha na operação! Valor inválido.")

    elif menu == "e":
       
        print(' EXTRATO '.center(50, '='))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(''.center(50, '='))

    elif menu == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        