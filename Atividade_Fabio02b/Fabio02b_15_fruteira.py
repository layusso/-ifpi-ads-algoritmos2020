def main():
    morango, maca = map(float, input('Quantidade em kg de maçã e morango que deseja:').split(' '))
    strawberry = valor_morango(morango)
    apple = valor_maca(maca)
    total = strawberry + apple
    kg_totais = morango + maca

    if kg_totais > 8 or total > 25:
        total_descontado = total-(total*0.10)
        print('O valor a pagar será de R$:', total_descontado)
    else:
        print('O valor a pagar será de R$:', total)


def valor_morango(morango):
    if morango <= 5:
        valor = morango*2.5
        return valor
    elif morango > 5:
        valor = morango*2.2
        return valor


def valor_maca(maca):
    if maca <= 5:
        valor = maca*1.8
        return valor
    elif maca > 5:
        valor = maca*1.5
        return valor


main()
