def main():
    numero = int(input('Numero: '))

    c = numero // 100
    d = numero % 100 // 10
    u = numero % 100 % 10

    saida = ''
    if c > 0:
        saida = saida + str(c) + ' centena' + tem_s(c)
    if d > 0:
        saida += sep_dezenas(c, u) + str(d) + ' dezena' + tem_s(d)
    if u > 0:
        saida += sep_unidades(c, d) + str(u) + ' unidade' + tem_s(u)

    print(saida)


def tem_s(valor):
    return 's' if valor > 1 else ''


def sep_unidades(c, d):
    if c > 0 or d > 0:
        return ' e '
    else:
        return ''


def sep_dezenas(c, u):
    if c == 0:
        return ''
    elif u > 0:
        return ', '
    else:
        return ' e '

if __name__ == "__main__":
    main()