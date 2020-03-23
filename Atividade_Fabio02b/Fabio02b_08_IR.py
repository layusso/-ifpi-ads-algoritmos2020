def main():
    horas, dqt = map(float, input('Valor da hora e a quantidade de horas:').split(' '))
    salario(horas, qtd)

def salario(horas, qtd):
    salario = horas * qtd
    if salario <= 900:
        ir = 0
        inss = salario*0.08
        fgts = salario*0.11
        descontos = inss + ir
        liquido = salario - descontos
        print(f'Salário bruto ({horas} * {qtd}): R$ {salario}')
        print(f'(-) IR (isento)')
        print(f'INSS (8%): R$ {inss}')
        print(f'FGTS(11%): R$ {fgts}')
        print(f'Total de descontos: R$ {descontos}')
        print(f'Salário Liquido: {liquido}')

    elif 900 < salario <= 1500:
        ir = salario * 0.05
        inss = salario*0.8
        fgts = salario*0.11
        descontos = inss + ir
        liquido = salario - descontos
        print(f'Salário bruto ({horas} * {qtd}): R$ {salario}')
        print(f'(-) IR (5%): R$ {ir}')
        print(f'INSS (8%): R$ {inss}')
        print(f'FGTS(11%): R$ {fgts}')
        print(f'Total de descontos: R$ {descontos}')
        print(f'Salário Liquido: {liquido}') 
    
    elif 1500 < salario <= 2500:
        ir = salario * 0.10
        inss = salario*0.09
        fgts = salario*0.11
        descontos = inss + ir
        liquido = salario - descontos
        print(f'Salário bruto ({horas} * {qtd}): R$ {salario}')
        print(f'(-) IR (10%): R$ {ir}')
        print(f'INSS (9%): R$ {inss}')
        print(f'FGTS(11%): R$ {fgts}')
        print(f'Total de descontos: R$ {descontos}')
        print(f'Salário Liquido: {liquido}') 
    
    elif 2500 < salario:
        ir = salario * 0.20
        inss = salario*0.11
        fgts = salario*0.11
        descontos = inss + ir
        liquido = salario - descontos
        print(f'Salário bruto ({horas} * {qtd}): R$ {salario}')
        print(f'(-) IR (20%): R$ {ir}')
        print(f'INSS (11%): R$ {inss}')
        print(f'FGTS(11%): R$ {fgts}')
        print(f'Total de descontos: R$ {descontos}')
        print(f'Salário Liquido: {liquido}') 


main()
