def triangulo():
    angulo_1 = float(input('Insira o primeiro ângulo:'))
    angulo_2 = float(input('Insira o segundo ângulo:'))
    angulo_3 = float(input('Insira o terceiro ângulo;'))
    soma_angulos = angulo_1 + angulo_2 + angulo_3
    
    
    
    if soma_angulos != 180
            print('Não forma um triângulo.')
    elif angulo_1 == 0 or angulo_2 == 0 or angulo_3 == 0:
            print('Não existe ângulo de 0 graus!')
    elif soma_angulos == 180 and angulo_1<90 and angulo_2<90 and angulo_3<90:
        print('Forma um triângulo acutângulo')
    elif soma_angulos == 180 and angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
        print('Forma um triângulo retângulo')
    elif soma_angulos == 180 and angulo_1 > 90 or angulo_2 > 90 or angulo_3 > 90:
        print('Forma um triângulo obtusângulo')
        

           
triangulo()
