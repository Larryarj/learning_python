# mostrar raiz quadrada
raiz = 1
num = int(input('digite um numero para ver sua raiz quadrada: '))

while True:
    
    if raiz * raiz == num:
        print(f'a raiz de {num} é: {raiz}')
        break
    
    else:
        raiz += 1
