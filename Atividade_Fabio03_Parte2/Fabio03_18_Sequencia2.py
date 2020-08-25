def main():
    n = int(input("Defina n: "))
    cont = 1
    n2 = n
    s = 0

    while cont <= n:
        s += cont / n2
        print(f"{cont}/{n2} + ")
        n2 -= 1
        cont += 1

        
        

    print(f"S = {s}")
main()