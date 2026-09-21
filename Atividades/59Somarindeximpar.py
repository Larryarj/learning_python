lista = []
qtd = int(input('quantos numeros voce quer somar? '))

for i in range(0 , qtd , 1):
    numero = int(input(f'digite o {i + 1} numero inteiro: '))
    lista.append(numero)

print(lista)

soma = 0

for j in range(0, len(lista), 1):
    if j % 2 != 0:
        soma += lista[j]

print(f'soma: {soma}')
