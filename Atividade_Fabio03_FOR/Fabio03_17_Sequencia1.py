def main():
    n = int(input("Defina n: "))
    s = 0

    for i in range(1, n+1):
        print(f"1/{i} + ", end=" ")
        s += 1/i

    print(f"S = {s}")
main()