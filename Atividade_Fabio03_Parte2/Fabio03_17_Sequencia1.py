def main():
    n = int(input("Defina n: "))
    cont = 1
    s = 0

    while cont <= n:
        print(f"1/{cont} + ", end=" ")
        cont += 1
        s += 1/cont

    print(f"S = {s}")
main()