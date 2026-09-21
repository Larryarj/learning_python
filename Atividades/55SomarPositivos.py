numeros = []
qtd = 0
while True:
    numero = int(input('digite um numero inteiro,positivo ou negativo: '))
    if numero > 0:
        numeros.append(numero)
        qtd += 1
    else:
        break

print(numeros)
print(f'media: {sum(numeros) / qtd}')
