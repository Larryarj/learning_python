numero = int(input('digite um numero inteiro para seber se ele é primo: '))
lista = []
for i in range(1 , numero +1 , 1):
    if numero % i == 0:
        lista.append(i)

if len(lista) == 2:
    print('primo')
else:
    print(f'não é primo. seus divisores:{lista}')
