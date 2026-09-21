matriz = [[42 , 17 , 89 , 63 , 11],
          [75 , 28 , 94 , 36 , 58],
          [7 , 81 , 49 , 22 , 97],
          [65 , 3 , 54 , 39 , 70]]

multiplicador = int(input('digite por quanto voce quer multiplicar a matriz: '))

for linha in range(0 , len(matriz) , 1):

    for coluna in range(0 , len(matriz[linha]) , 1):

        num_multiplicado = matriz[linha][coluna] * multiplicador

        matriz[linha][coluna] = num_multiplicado

print(matriz)
