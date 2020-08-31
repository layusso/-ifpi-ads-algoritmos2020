def main():
    n = int(input("Digite o valor de n: "))

    for i in range(1, n+1):
        if i ** 2 <= n:
            maior = i ** 2
    
    

    print(f"O maior quadrado é de {maior}")

main()