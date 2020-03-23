def imc():
    altura = float(input('Digite a sua altura:'))
    peso = float(input('Digite o seu peso:'))
    imc = peso / altura**2

    if imc <= 25:
        print('Seu peso é normal')
    elif 25 < imc <= 30:
        print('Obeso')
    elif imc > 30:
        print('Obesidade mórbia')

imc()