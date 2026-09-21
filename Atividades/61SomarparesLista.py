lista = []
for i in range(0 , 8 , 1):
    num = int(input('digite um numero inteiro: '))
    lista.append(num)

lista2 = []

for numero in lista:

    if numero % 2 == 0:
        lista2.append(numero)

print(f'soma dos pares: {sum(lista2)}')
