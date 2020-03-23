def maior():
    numero_1 = float(input('Insira o primeiro número:'))
    numero_2 = float(input('Insira o terceiro número:'))
    numero_3 = float(input('Insira o terceiro número:'))

    if numero_1 > numero_2 and numero_3:
        print('O maior é o primeiro número.')
    elif numero_2 > numero_1 and numero_3:
        print('O maior é o segundo número.')
    elif numero_3 > numero_1 and numero_2:
        print('O maior é o terceiro número.')
    else:
        print('Existem números iguais')


maior()