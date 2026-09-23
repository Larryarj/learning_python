num = int(input('digite um numero '))
soma = 0

for i in range(num + 1):
    if (i <= num) and (i%2 == 0):
        soma += i

print(soma)
