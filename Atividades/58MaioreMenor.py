lista = []

for i in range(0 , 10 , 1):
    qtd = int(input('digite um numero inteiro: '))
    lista.append(qtd)

print(lista)

# Inicializa 'maior' e 'menor' com o primeiro elemento da lista
# Isso garante que eles tenham um valor válido para comparação
maior = lista[0]
menor = lista[0]

# Itera sobre o restante da lista para encontrar o verdadeiro maior e menor
for numero in lista:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f'maior: {maior}')
print(f'menor: {menor}')
