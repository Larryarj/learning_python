numero = int(input('digite um numero inteiro, para calcular seu fatorial: '))
fatorial = 1

for i in range(1 , numero , 1):
    fatorial += i * fatorial

print(fatorial)
