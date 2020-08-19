def main():
    n = int(input("Informe a quantidade de números: "))
    cont = 0
    soma = 0

    while cont < n:
        numero = float(input("Digite um número: "))
        soma += numero
        cont += 1
    
    media = soma / n

    print(f"A soma dos números é {soma} e média {media}")

main()