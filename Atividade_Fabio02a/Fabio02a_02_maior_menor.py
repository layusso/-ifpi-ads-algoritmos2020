def maior_menor():
    numero_1 = float(input('Insira o primeiro número:'))
    numero_2 = float(input('Insira o segundo número:'))

    if numero_1 > numero_2:
        print('{} é maior que {}'.format(numero_1, numero_2))
    elif numero_2 > numero_1:
        print('{} é maior que {}'.format(numero_2, numero_1))
    elif numero_1 == numero_2:
        print('Os números são iguais')
    

maior_menor()