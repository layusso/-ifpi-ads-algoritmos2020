def igualdade():
    numero_1 = float(input('Digite o primeiro número:'))
    numero_2 = float(input('Digite o segundo número:'))
    numero_3 = float(input('Digite o terceiro número:'))

    if numero_1 == numero_2 == numero_3:
        print('Existem 3 números iguais.')
    elif numero_1 == numero_2 != numero_3 or numero_3 == numero_2 != numero_1 or numero_3 == numero_1 != numero_2:
        print('2 números iguais.')
    else:
        print('Todos os números são diferentes.')


igualdade()
