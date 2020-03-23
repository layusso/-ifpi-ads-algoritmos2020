def retangulo():
    x = float(input('Insira o ponto x:'))
    y = float(input('Insira o ponto y:'))
    area = x * y
    if area < 0 :
        print('A área não pode ser negativa:')
    else:
        print(f'Forma um triângulo de área {area}')
    
retangulo()