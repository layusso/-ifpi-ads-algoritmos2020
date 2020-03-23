def opcao():
    opcao = int(input('Escolha um número de 1 a 3'))
    num_1 = float(input('Insira o primeiro número:'))
    num_2 = float(input('Insira o segundo número:'))
    num_3 = float(input('Insira o terceira número:'))

    if opcao == 1:
        print(f'{num_1}')
    elif opcao == 2:
        print(f'{num_2}')
    elif opcao == 3:
        print(f'{num_3}')
    else:
        print('Sua opção foi diferente de um número de 1 a 3!')

opcao()