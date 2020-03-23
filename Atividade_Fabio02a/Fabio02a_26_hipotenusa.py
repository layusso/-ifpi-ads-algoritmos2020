def lados():
    ladoa = float(input('Digite o valor do primeiro lado:'))
    ladob = float(input('Digite o valor do segundo lado:'))
    ladoc = float(input('Digite o valor do terceiro lado:'))
    if ladoa == (ladob ** 2 + ladoc**2)**(1/2):
        print('Lado a é a hipotenusa e os demais são catetos')
    elif ladob == (ladoa**2 + ladoc**2)**(1/2):
        print('Lado b é a hipotenusa e os demais são catetos')
    elif ladoc == (ladoa**2 + ladob**2)**(1/2):
        print('Lado c é a hipotenusa e os demais são catetos')
    else:
        print('Essas medidas não correspondem a um triângulo retângulo!')

lados()
