def idade():
    dia_atual = int(input('Insira o dia atual:'))
    mes_atual = int(input('Insira o mês atual:'))
    ano_atual = int(input('Insira o ano atual:'))
    dia_nasc = int(input('Insira o dia do seu nascimento:'))
    mes_nasc = int(input('Insira o mês do seu nascimento:'))
    ano_nasc = int(input('Insira o ano do seu nascimento:'))
    idade = ano_atual - ano_nasc
    quase_idade = idade - 1

    if dia_atual >= dia_nasc and mes_atual >= mes_nasc:
        print('Você tem {} anos'. format(idade))
    else:
        print(f'Você tem {quase_idade} anos.')

idade()

