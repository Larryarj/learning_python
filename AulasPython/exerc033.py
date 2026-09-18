numeros = []

for i in range(3):
    numero = int(input(f'digite o numero {i +1}: '))
    numeros.append(numero)

print(f"maior numero: {max(numeros)}")
print(f"menor numero: {min(numeros)}")
