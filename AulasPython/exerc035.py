a = int(input('digite o tamanho do lado A do triangulo '))
b = int(input('digite o tamanho do lado b do triangulo '))
c = int(input('digite o tamanho do lado c do triangulo '))

if (a + b) >= c and (b + c) >= a and (a + c) >= b:
    print('seu triangulo é possivel')
else:
    print('isso não forma um triangulo.')
