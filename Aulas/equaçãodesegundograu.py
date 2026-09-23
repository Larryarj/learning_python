parada = 0

while parada == 0:
    a = float(input('digite a '))
    b = float(input('digite b '))
    c = float(input('digite c '))

    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        print (x1 , x2 )

    elif delta == 0:
        x = -b / (2*a )
        print('seu delta é = 0, x=', x)

    else:
        print('seu delta é negativo, logo não existe raiz REAL ' )

    parada = int(input('quer resolver outra? digite 0 para sim ou 1 para não '))
