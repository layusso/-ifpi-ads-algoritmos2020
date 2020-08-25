def main():
    n = int(input("Defina n: "))
    cont = 1
    cont2 = 0
    s = 0

    while cont <= n:
        valor = n - cont2
        if cont % 2 == 0:
            s -= valor/cont
            print(f"- {valor}/{cont}", end=" ")

        else:    
            s += cont/valor
            print(f"+ {cont}/{valor}", end=" ")
        
        cont += 1
        cont2 += 1
        
    print(f"S = {s}")

main()