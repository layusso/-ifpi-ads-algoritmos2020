def main():
    info = input('Informe o tipo e a quantidade de carne:').split(' ')
    pagamento = input('Qual a forma de pagamento (cartão ou dinheiro)?:')
    tipo = info[0]
    qtd = float(info[1])
    if tipo == 'file':
       total = carne_file(qtd)
       nota(tipo, qtd, pagamento, total)
    elif tipo == 'alcatra':
        total = carne_alcatra(qtd)
        nota(tipo, qtd, pagamento, total)
    elif tipo == 'picanha':
        total = carne_picanha(qtd)
        nota(tipo, qtd, pagamento, total)


def carne_file(qtd):
    if qtd <= 5:
        valor = qtd*4.9
        return valor
    elif qtd > 5:
        valor = qtd*5.8
        return valor


def carne_alcatra(qtd):
    if qtd <= 5:
        valor = qtd*5.9
        return valor
    elif qtd > 5:
        valor = qtd*6.8
        return valor


def carne_picanha(qtd):
    if qtd <= 5:
        valor = qtd*6.9
        return valor
    elif qtd > 5:
        valor = qtd*7.8
        return valor


def descontos(total):
    valor = total-(total*0.05)
    return valor


def nota(tipo, qtd, pagamento, total):
    print(f'Carne: {tipo}.')
    print(f'Qunatidade: {qtd} Kg.')
    print(f'Tipo de pagamento: {pagamento}')
    print(f'Valor total: R$ {total}')
    if pagamento == 'cartão':
        print('Desconto 5%')
        desconto = descontos(total)
        print(f'Valor a pagar: R${desconto}')
    elif pagamento == 'dinheiro':
        print('Sem descontos')
    

    
    




main()
