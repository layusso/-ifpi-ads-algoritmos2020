def main():
    n = int(input('Informe a quantidade de funcionários: '))
    valor_hora = 12
    inss = 0.085
    ir = 0.05

    for i in range(1, n+1):
        horas_trabalhadas = int(input("Informe quantas horas trabalhadas: "))
        dependentes = int(input("Número de dependentes: "))

        valor_dependentes = dependentes * 40

        salario = (valor_hora * horas_trabalhadas) + valor_dependentes
        inss_desc = salario * inss
        ir_desc = salario * ir
        salario_liquido = salario - inss_desc - ir_desc

        print(f"Salario liquido: R${salario_liquido:.2f}, INSS: R${inss_desc:.2f}, IR: R${ir_desc:.2f}")


main()