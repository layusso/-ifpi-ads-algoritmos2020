def primo():
    numero = int(input('Escolha um número de 0 a 100'))

    if numero == 2:
        print('O número é primo')
    elif numero == 3:
        print('O número é primo')
    elif numero == 5:
        print('O número é primo')
    elif numero == 7:
        print('O número é primo')
    elif numero % 2 == 0:
        print('O número não é primo')
    elif numero % 3 == 0:
        print('O número não é primo')
    elif numero % 5 == 0:
        print('O número não é primo')
    elif numero % 7 == 0:
        print('O número não é primo')
    else:
        print('O numero é primo')


numero()