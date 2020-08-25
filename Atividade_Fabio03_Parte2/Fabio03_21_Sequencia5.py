def main():
    cont = 0
    n = 1
    s = 0

    while n <= 99:
        if n % 2 != 0:
            cont += 1
            s += n / cont
            print(f" + {n}/{cont}", end=" ")

        n += 1

    print(f"S = {s}")

main()
