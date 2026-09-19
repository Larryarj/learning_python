cordenadax = int(input('digite a coordenada x:'))
cordenaday = int(input('digite a coordenada y:'))

if cordenadax > 0 and cordenaday > 0:
    print('primeiro quadrante')

elif cordenadax < 0 and cordenaday > 0:
    print('segundo quadrante')

elif cordenadax < 0 and cordenaday < 0:
    print('terceiro quadrante')

elif cordenadax > 0 and cordenaday < 0:
    print('quarto quadrante')
    