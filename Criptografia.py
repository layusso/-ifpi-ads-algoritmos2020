
def main():
    n = int(input(""))
    cont = 0

    while cont < n:
        string = input("")
        string_invertida = inverter(rotate_word(string))
        metade = rotacionar_metade(string_invertida)
        cont += 1
        print(metade)

def rotate_word(texto):
    palavra = ""
    for i in range(len(texto)):
        if for_letra(texto[i]):
            nova_letra = chr(ord(texto[i]) + 3)
            palavra += nova_letra
        
        else:
            palavra += texto[i]

    return palavra



def for_letra(letra):
    if 65 <= ord(letra) <= 90 or 97 <= ord(letra) <= 122:
        return True
    
    else:
        return False

def inverter(palavra):
    
    return palavra[::-1]


def rotacionar_metade(word):
    index = (len(word) // 2)
    parte = word[0:index]
    metade = ""
    metade_rotacionada = ""
    while index < len(word):
        metade += word[index]
        index += 1
    
    for i in range(len(metade)):
        nova_letra = chr(ord(metade[i]) - 1)
        metade_rotacionada += nova_letra


    palavra = parte + metade_rotacionada 
    return palavra


main()