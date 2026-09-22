parar = 0

while parar == 0 :
    numero = int(input('digite um numero:'))
    resto = numero % 2

    if resto == 0 :
        print ('seu numero é par')

    else:
        print('seu numero é impar') 
    
    parar = int(input('para continuar digite 0,para terminar digite 1:'))
    