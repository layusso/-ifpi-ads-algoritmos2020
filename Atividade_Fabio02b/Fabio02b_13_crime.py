def main():
    print("Responda com 's' para sim, e 'n' para não")
    a = input("Telefonou para a vítima? ")
    b = input("Esteve no local do crime? ")
    c = input("Mora perto da vítima? ")
    d = input("Devia para a vítima? ")
    e = input("Já trabalhou com a vitima? ")
    resultado(contador(a, b, c, d, e))


def contador(a, b, c, d, e):
    contador = 0
    if a == "s":
        contador += 1
    if b == "s":
        contador += 1
    if c == "s":
        contador += 1
    if d == "s":
        contador += 1
    if e == "s":
        contador += 1

    return contador

def resultado(contador):
    if contador < 2:
        print("Inocente")
    elif contador == 2:
        print("Suspeito")
    elif 3 <= contador <= 4:
        print("Cumplice")
    elif contador == 5:
        print("Assassino") 

main()