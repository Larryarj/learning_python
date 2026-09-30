# calcular frete com base na distancia e tipo de produto

while True:
    
    distancia = float(input('qual a distancia da entrega? '))
    tipo_produto = int(input('qual o tipo de produto, digite 1 para fragil, 2 para perecivel e 3 para normal '))
    
    # validar dados

    if distancia <= 0:
        print('distancia invalida, tente novamente')
        continue
    
    if tipo_produto != 1 and tipo_produto != 2 and tipo_produto != 3:
        print('digite um tipo válido')
        continue
    
    #calcular valor base

    if distancia > 0 and distancia < 100 :
        valorbase = distancia * (0.50)
        

    elif distancia >= 101 and distancia <= 500 :
        valorbase = distancia * (0.75)

    else:
        valorbase = distancia * (1.1)

    #calcular taxa por tipo

    if tipo_produto == 1:
        taxa_por_tipo = valorbase * (1.2)

    elif tipo_produto == 2:
        taxa_por_tipo = valorbase * (1.35)

    elif tipo_produto == 3:
        taxa_por_tipo = valorbase + 0

    print('o valor base é: ' , valorbase , 'e o preço total é: ' , taxa_por_tipo )
    
    continue


# finalizado