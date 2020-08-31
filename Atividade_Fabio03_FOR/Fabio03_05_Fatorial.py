def main():
    numero = int(input("Digite um número: "))
    valor = 1

    for i in range(1, numero+1):
        valor = valor * i

    print(f"O fatorial de {numero} é {valor}")

main()