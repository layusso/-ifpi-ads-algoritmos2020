def main():
    limite_i = int(input("Determine o limite inferior: "))
    limite_s = int(input("Determine o limite superior: "))

    for i in range(limite_i, limite_s+1):
        if i % 2 != 0:
            print(i)


main()