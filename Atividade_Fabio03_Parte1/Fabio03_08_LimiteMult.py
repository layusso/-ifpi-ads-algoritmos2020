def main():
    limite_i = int(input("Determine o limite inferior: "))
    limite_s = int(input("Determine o limite superior: "))
    n = int(input("Determine o valor de n: "))

    while limite_i <= limite_s:
        if limite_i % n == 0:
            print(limite_i)

        limite_i += 1


main()