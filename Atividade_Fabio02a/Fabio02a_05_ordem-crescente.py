def ordem():
    numero_1 = float(input('Digite o primeiro número:'))
    numero_2 = float(input('Digite o segundo número:'))
    numero_3 = float(input('Digite o terceiro número:'))

    if numero_1 < numero_2 < numero_3:
        print('Ordem crescente: {}, {}, {}.'.format(numero_1, numero_2, numero_3))
    elif numero_1 < numero_3 < numero_2:
         print('Ordem crescente: {}, {}, {}.'.format(numero_1, numero_3, numero_2))
    elif numero_2 < numero_3 < numero_1:
         print('Ordem crescente: {}, {}, {}.'.format(numero_2, numero_3, numero_1))
    elif numero_2 < numero_1 < numero_3:
         print('Ordem crescente: {}, {}, {}.'.format(numero_2, numero_1, numero_3))
    elif numero_3 < numero_1 < numero_2:
         print('Ordem crescente: {}, {}, {}.'.format(numero_3, numero_1, numero_2))
    elif numero_3 < numero_2 < numero_1:
         print('Ordem crescente: {}, {}, {}.'.format(numero_3, numero_2, numero_1))
    else: 
        print('Existem números iguais.')


ordem()
