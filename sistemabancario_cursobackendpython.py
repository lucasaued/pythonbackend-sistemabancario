menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Erro. O valor informado é inválido.")

    elif opcao == "2":
        
        excedeu_saques = num_saques == LIMITE_SAQUES
        if not excedeu_saques:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            if excedeu_saldo:
                print("Erro. Saldo suficiente.")

            elif excedeu_limite:
                print("Erro. O valor do saque excede o limite.")

            elif valor > 0:
                saldo-= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                num_saques+=1

            else:
                print("Erro. O valor informado é inválido.")
                
        else:
            print("Erro. Número máximo de saques excedido.")
            

    elif opcao == "3":
        print(" Extrato ".center(36,"-"))
        print(f"\n{extrato}" if extrato else "\nNenhuma operação foi realizada.")
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("".center(36,"-"))

    elif opcao == "0":
        print("Saindo do sistema.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")