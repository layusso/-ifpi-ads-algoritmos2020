def main():
    salario = float(input('Digite o valor do seu salário:'))
    aumento(salario)


def aumento(salario):
    if salario <= 280:
        porcentagem = '20%'
        valor = (salario*0.20)
        total = valor + salario
        print(f'Salário: {salario}')
        print(f'Percentual de aumento: {porcentagem}')
        print(f'Valor do aumento: {valor}')
        print(f'Novo salário: {total}')

    elif 280 < salario <= 700:
        porcentagem = '15%'
        valor = (salario*0.15)
        total = valor + salario
        print(f'Salário: {salario}')
        print(f'Percentual de aumento: {porcentagem}')
        print(f'Valor do aumento: {valor}')
        print(f'Novo salário: {total}')

    elif 700 < salario <= 1500:
        porcentagem = '10%'
        valor = (salario*0.10)
        total = valor + salario
        print(f'Salário: {salario}')
        print(f'Percentual de aumento: {porcentagem}')
        print(f'Valor do aumento: {valor}')
        print(f'Novo salário: {total}')

    elif salario > 1500:
        porcentagem = '5%'
        valor = (salario*0.05)
        total = valor + salario
        print(f'Salário: {salario}')
        print(f'Percentual de aumento: {porcentagem}')
        print(f'Valor do aumento: {valor}')
        print(f'Novo salário: {total}')


main()
