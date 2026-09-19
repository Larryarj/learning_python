numeros = []

for i in range(0 , 3 , 1):
    num = int(input('digite um numero inteiro: '))
    numeros.append(num)
print(numeros)

for numero in range(1 , len(numeros) , 1):

    if numeros[numero] > numeros[numero -1]:
        maior = numeros[numero]

print(maior)
