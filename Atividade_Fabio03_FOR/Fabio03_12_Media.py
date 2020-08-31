def main():
    n = int(input("Informe a quantidade de números: "))
    soma = 0

    for i in range(1, n+1):
        numero = float(input("Digite um número: "))
        soma += numero
    
    media = soma / n

    print(f"A soma dos números é {soma} e média {media:.2f}")

main()