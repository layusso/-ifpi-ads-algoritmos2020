def main():
    ni = int(input("Digite o numero inicial: "))
    razao = int(input('Razão: '))
    limite = int(input('Limite da P.A: '))
    progressao(ni, razao, limite)


def progressao(a0, r, limite):
    num_pa = a0
    for i in range(num_pa, limite+1):
        num_pa += r
        if num_pa < limite:
            print(num_pa, end=' ')


main()