lista1 = []

for i in range(0 , 5 , 1):
    num = int(input('digite um numero inteiro: '))
    lista1.append(num)

print(lista1)
lista2 = []

for j in range(0 , len(lista1) , 1):

    lista2.append(lista1[j] * 2)

print(lista2)
