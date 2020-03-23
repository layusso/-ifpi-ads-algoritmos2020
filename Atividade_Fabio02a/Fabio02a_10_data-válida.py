def main():
    dia, mes, ano = map(int, input().split('/'))

    if data_valida(dia, mes, ano):
        print('Data válida')
    else:
        print('Data inválida')


def data_valida(d: int, m: int, ano: int) -> bool:  # booleana
    if ano > 0 and mes_valido(m) and \
            dia_valido(d, m, ano) == True:         
        return True
    else:
        return False


def dia_valido(d, m, a):
    if d < 1 or d > 31:
        return False

    if m < 8:  # JAN - JUL
        if m % 2 == 0:  # par
            if m != 2:
                return True if d <= 30 else False
            else:  # FEV*
                if eh_bissexto(a) == True:
                    return True if d <= 29 else False
                else:
                    return True if d <= 28 else False

        else:  # impar
            return True if d <= 31 else False
    else:  # AGO - DEZ
        if m % 2 == 0:  # par
            return True if d <= 31 else False
        else: # impar
            return True if d <= 30 else False


def mes_valido(mes):
    #return mes >= 1 and mes <= 12
    if mes >= 1 and mes <= 12:
        return True
    else:
        return False


def eh_bissexto(ano):
    # return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False


main()