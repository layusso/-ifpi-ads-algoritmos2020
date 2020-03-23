def idade():
    dia_nasc = int(input('O dia que você nasceu:'))
    mes_nasc = int(input('O mês  que você nasceu:'))
    ano_nasc = int(input('O ano em que você nasceu:'))
    dia_atual = int(input('Dia atual:'))
    mes_atual = int(input('Mês atual:'))
    ano_atual = int(input('Ano atual:'))


    idade_dia = dia_atual - dia_nasc
    idade_mes = mes_atual - mes_nasc
    idade = ano_atual - ano_nasc
    idade_diadia = dia_nasc - dia_atual
    idade_mesmes = mes_nasc - mes_atual

    if dia_nasc == dia_atual and mes_nasc == mes_atual:
        print(f'Você tem {idade} anos')
    elif dia_nasc < dia_atual and mes_nasc == mes_atual:
        print(f'Você tem {idade}, 0 meses e {idade_dia} dias')
    elif dia_nasc < dia_atual and mes_nasc < mes_atual:
        print(f'Você tem {idade} anos, {idade_mes} meses e {idade_dia} dias')
    elif dia_nasc > dia_atual and mes_atual == mes_nasc:
        print(f'Você tem {idade} anos, 0 meses e {idade_diadia} dias.')
    elif dia_nasc > dia_atual and mes_nasc > mes_atual:
        print(f'Você tem {idade - 1} anos, {idade_mesmes} meses e {idade_diadia} dias.')
    elif dia_atual == dia_atual and mes_nasc > mes_atual:
        print(f'Você tem {idade - 1 } anos, {idade_mesmes} meses e 0 dias')
    elif dia_atual == dia_nasc and mes_atual > mes_nasc:
        print(f'Você tem {idade} anos, {idade_mes} meses e 0 dias')

idade()