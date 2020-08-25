def main():
    n = int(input("Defina n: "))
    cont = 1
    s = 1

    print(f"1/{cont}", end=" ")
    while cont < n:
        cont += 1
        if cont % 2 == 0:
            s -= 1/cont
            print(f"- 1/{cont}", end=" ")

        else:    
            s += 1/cont
            print(f"+ 1/{cont}", end=" ")

    print(f"S = {s}")
main()