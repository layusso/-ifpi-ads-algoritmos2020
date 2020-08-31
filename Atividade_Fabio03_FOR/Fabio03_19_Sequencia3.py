def main():
    n = int(input("Defina n: "))
    cont2 = 0
    s = 0

    for i in range(1, n+1):
        valor = n - cont2
        if i % 2 == 0:
            s -= valor/i
            print(f"- {valor}/{i}", end=" ")

        else:    
            s += i/valor
            print(f"+ {i}/{valor}", end=" ")
        
        cont2 += 1
        
    print(f"S = {s}")

main()