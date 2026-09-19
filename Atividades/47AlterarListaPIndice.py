numeros = []
for i in range(0 , 3, 1):
  num = int(input('digite um numero inteiro: '))
  numeros.append(num)

print(numeros)

primeiro = numeros[0]
segundo = numeros[1]
terceiro = numeros[2]

numeros.pop(0)
numeros.insert(0 , terceiro)

numeros.pop(1)
numeros.insert(1 , segundo)

numeros.pop(2)
numeros.insert(2 , primeiro)

print(numeros)
