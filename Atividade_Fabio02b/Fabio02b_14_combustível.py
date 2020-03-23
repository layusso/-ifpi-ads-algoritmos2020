def main():
    litros = float(input('Quantos litros de combstível?:'))
    tipo = input('Escolha o tipo de combustivel. Digite A para álcool e G para gasolina:')

    if tipo == 'A':
        valor_pg = alcool(litros)
        print('Valor a pagar: R$', valor_pg)
    elif tipo == 'G':
        valor_pg = gasolina(litros)
        print('Valor a pagar: R$', valor_pg)


def alcool(litros):
    if litros <= 20:
        valor = litros*(1.90*0.03)
        return valor
    elif litros > 20:
        valor = litros*(1.90*0.05)
        return valor


def gasolina(litros):
    if litros <= 20:
        valor = litros*(2.5*0.04)
        return valor
    elif litros > 20:
        valor = litros*(2.5*0.06)
        return valor


main()
