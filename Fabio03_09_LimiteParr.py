def main():
    limite_i = int(input("Determine o limite inferior: "))
    limite_s = int(input("Determine o limite superior: "))

    while limite_i <= limite_s:
        if limite_i % 2 == 0:
            print(limite_i)

        limite_i += 1


main()