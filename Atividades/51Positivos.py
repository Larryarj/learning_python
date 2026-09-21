positivos = []

for i in range(0 , 10 , 1):
    numero = int(input('digite um numero inteiro, positivo ou negativo: '))
    if numero > 0:
      positivos.append(numero)

print(positivos)
