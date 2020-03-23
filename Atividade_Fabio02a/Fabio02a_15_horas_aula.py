def horas_aula():
    hora_1 = float(input('Horas trabalhadas do primeiro professor:'))
    valor = float(input('Valor da hora aula do primeiro professor:'))
    hora_2 = float(input('Horas trabalhadas do segundo professor:'))
    valor_2 = float(input('Valor da hora aula do segundo professor:'))
    salário_total1 = hora_1 * valor
    salário_total2 = hora_2 * valor_2

    if salário_total1 > salário_total2:
        print('O salário total do primeiro professor é maior')
    elif salário_total2 > salário_total1:
        print('O salário total do segundo professor é maior')
    elif salário_total1 == salário_total2:
        print('O salário de ambos são iguais.')
    
horas_aula()
