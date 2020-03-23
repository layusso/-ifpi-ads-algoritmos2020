def main():
    hora_inicial = int(input('Digite a hora de início de jogo: '))
    minuto_inicial = int(input('Digite os minutos de ínicio de jogo: '))
    hora_final = int(input('Digite a hora de fim de jogo: '))
    minuto_final = int(input('Digite os minutos de fim de jogo: '))
    hora_jogo(hora_inicial, hora_final, minuto_inicial, minuto_final)


def hora_jogo(val_1, val_2, val_3, val_4):
    '''
    Mostra a duração em horas e minutos de acordo com a o tempo inicial
    e o tempo final
    '''
    if val_1 > 23 or val_2 > 23 or val_3 > 59 or val_4 > 59:
        print('ERRO DADOS INVÁLIDOS PROCESSO DE AUTODESTRUIÇÃO DO COMPUTADOR')
    if val_1 < val_2 and val_3 <= val_4:
        hora = val_2 - val_1
        minuto = val_3 - val_4
        print(f'Duração: {hora} hora(s) e {minuto} minuto(s)')
    elif val_1 < val_2 and val_3 > val_4:
        hora = (val_2 - val_1) - 1
        minuto = (60 - val_3) + val_4
        print(f'Duração: {hora} hora(s) e {minuto} minuto(s)')
    elif val_1 > val_2 and val_3 > val_4:
        hora = (24 - val_1) + val_2 - 1
        minuto = (60 - val_3) + val_4
        print(f'Duração: {hora} hora(s) e {minuto} minuto(s)')
    elif val_1 > val_2 and val_3 < val_4:
        hora = (24 - val_1) + val_2
        minuto = val_4 - val_3
        print(f'Duração: {hora} hora(s) e {minuto} minuto(s)')
    elif val_1 == val_2 and val_3 == val_4:
        print(f'Duração: 24 Horas')


main()