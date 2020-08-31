def main():
    n = int(input("Defina n: "))
    cont = 1
    s = 1

    for i in range(1, n+1):
        if i % 2 == 0:
            s -= 1/i
            print(f"- 1/{i}", end=" ")

        else:    
            s += 1/i
            print(f"+ 1/{i}", end=" ")

    print(f"S = {s}")
main()