def main():
    n = int(input("Informe a quantidade de números: "))
    cont = 0
    maior = 0
    menor = 78459875

    while cont < n:
        numero = float(input("Digite um número: "))
        if numero > maior:
            maior = numero
        
        elif numero < menor:
            menor = numero
        cont += 1
    
    print(f"O maior número é {maior} e o menor {menor}")


main()