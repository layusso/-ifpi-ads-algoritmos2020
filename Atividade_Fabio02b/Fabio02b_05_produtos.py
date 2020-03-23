def main():
    valor = input('Digite o valor de 3 produtos:').split(' ')
    map(float, valor)
     
    if valor[2] < valor[1] and valor[2] < valor[0]:
         print('Você deveria comprar o terceiro produto.')
    elif valor[1] < valor [2] and valor [1] < valor[0]:
        print('Você deveria comprar o segundo produto')
    elif valor[0] < valor[1] and valor[0] < valor[2]:
        print('Você deveria comprar o primeiro produto')



main()
