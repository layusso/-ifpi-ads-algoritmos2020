def main():
    n = int(input("Informe o número de habitantes: "))
    total_salario = 0
    total_filhos = 0
    total_1000 = 0
    cont = 0

    while cont < n:
        salario = float(input("Informe o salário: "))
        filhos = int(input("Informe a quantidade de filhos: "))

        total_salario += salario
        total_filhos += filhos

        if salario <= 1000:
            total_1000 += 1
        
        cont += 1
    

    media_salarial = total_salario / n
    media_filhos = total_filhos / n
    percentual = (total_1000 * 100) / n
    print(f"Media salarial da população: R${media_salarial:.2f}")
    print(f"Media filhos da população: {media_filhos:.2f}")
    print(f"Percentual de salários até R$1000 da população: {percentual:.2f}%")
main()