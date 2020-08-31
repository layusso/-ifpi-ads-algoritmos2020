def main():
    limite_i = int(input("Determine o limite inferior: "))
    limite_s = int(input("Determine o limite superior: "))

    cont = 0
    
    for i in range(1, limite_s+1):
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i)
            
        elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or \
                i % 7 == 0 or i % 11 == 0 or i % 13 == 0:
                cont += 1

        else:
            print(i)


main()