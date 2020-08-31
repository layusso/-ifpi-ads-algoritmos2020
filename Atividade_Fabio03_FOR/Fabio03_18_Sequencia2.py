def main():
    n = int(input("Defina n: "))
    n2 = n
    s = 0

    for i in range(1, n+1):
        s += i / n2
        print(f"{i}/{n2} + ")
        n2 -= 1

        
        

    print(f"S = {s}")
main()