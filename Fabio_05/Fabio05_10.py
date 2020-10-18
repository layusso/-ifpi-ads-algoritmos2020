def main():

    t1 = 0
    t2 = 1
    cont = 3
    n = int(input("Escreva o valor de números da sequencia: "))

    print(f"{t1}, {t2}", end='')

    while cont <= n:
        t3 = t1 + t2
        print(f"{t3}, ", end='')
        t1 = t2
        t2 = t3
        cont += 1

main()