def data():
    dia_1 = int(input('Insira o dia da primeira data:'))
    mes_1 = int(input('Insira o mês da primeira data:'))
    ano_1 = int(input('Insira o ano da primeira data:'))
    dia_2 = int(input('Insira o dia da segunda data:'))
    mes_2 = int(input('Insira o mês da segunda data:'))
    ano_2 = int(input('Insira o ano da segunda data:'))

    if ano_1 > ano_2:
        print('A primeira data é mais recente.')
    elif ano_2 > ano_1:
        print('A segunda data é mais recente.')
    elif ano_1 == ano_2 and mes_1 > mes_2:
        print('A primeira data é mais recente.')
    elif ano_1 == ano_2 and mes_2 > mes_1:
        print('A segunda data é mais recente.')
    elif ano_1 == ano_2 and mes_1 == mes_2 and dia_1 > dia_2:
        print('A primeira data é mais recente:')
    elif ano_1 == ano_2 and mes_1 == mes_2 and dia_1 < dia_2:
        print('A segunda data é mais recente.')

data()