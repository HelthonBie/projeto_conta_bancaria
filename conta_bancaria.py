menu = '''
====================== Menu ======================

[1] Depositar                [3] Exibir Extrato
[2] Sacar                    [4] Sair do programa

        Obrigado por usar nossos serviços!

==================================================
'''


saque_diario = 1500.0
saques_realizados = 0
saldo = 0
movimentacoes = []  # Lista para armazenar (depósitos e saques)

while True:
    print(menu)
    opcao = input('Digite o número da opção desejada: ')
    
    if opcao == '1':
        deposito = float(input('Digite o valor de depósito: '))
        if deposito >= 0:
            saldo += deposito
            movimentacoes.append(deposito)  
            print('Depósito efetuado com sucesso!')
        else:
            print('Valor informado não é aceito, tente novamente.')
            
    elif opcao == '2':
        if saques_realizados < 3:
            saque = int(input('Digite o valor do saque: '))
            if saque > 0 and saque <= saque_diario and saque <= saldo and saque<= 500:
                saldo -= saque
                saque_diario -= saque
                saques_realizados += 1
                movimentacoes.append(-saque)  
                print('Saque efetuado com sucesso!')
            else:
                print('Valor de saque inválido!')
        else:
            print('Você atingiu o limite de saques diários (3).')

    elif opcao == '3':
        if movimentacoes:
            print("Extrato:")
            for movimento in movimentacoes:
                if movimento > 0:
                    print(f"Depósito: R$ {movimento: .2f}")
                else:
                    print(f"Saque: R$ {abs(movimento): .2f}")
            print(f"Saldo atual: R$ {saldo: .2f}")
        else:
            print("Não foram realizadas movimentações.")
            
    elif opcao == '4':
        print("Saindo do programa...")
        break

    else:
        print('Opção inválida, tente novamente.')
