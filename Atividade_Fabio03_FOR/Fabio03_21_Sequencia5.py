def main():
    cont = 0
    s = 0

    for i in range(1, 100):
        if i % 2 != 0:
            cont += 1
            s += i / cont
            print(f" + {i}/{cont}", end=" ")


    print(f"S = {s}")

main()
