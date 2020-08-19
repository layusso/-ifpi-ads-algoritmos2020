def main():
    limite_i = int(input("Determine o limite inferior: "))
    limite_s = int(input("Determine o limite superior: "))
    contador = limite_i + 1

    while contador < limite_s:
        if contador == 2 or contador == 3 or contador == 5 or contador == 7:
            print(contador)
            contador += 1
        elif contador % 2 == 0 or contador % 3 == 0 or contador % 5 == 0 or \
                contador % 7 == 0 or contador % 11 == 0 or contador % 13 == 0:
            contador += 1
        else:
            print(contador)
            contador += 1


main()