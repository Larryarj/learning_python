matriz = [[42 , 17 , 89 , 63 , 11],
          [75 , 28 , 94 , 36 , 58],
          [7 , 81 , 49 , 22 , 97],
          [65 , 3 , 54 , 39 , 70]]

maior = 0

for linha in matriz:

    for numero in linha:

        if numero > maior:

            maior = numero

print(f'o maior numero é: {maior}')
