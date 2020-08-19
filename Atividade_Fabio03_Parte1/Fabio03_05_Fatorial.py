def main():
    numero = int(input("Digite um número: "))
    cont = 1
    valor = 1

    while cont <= numero:
        valor *= cont 
        cont += 1

    print(f"O fatorial de {numero} é {valor}")

main()