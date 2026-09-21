matriz = [[42 , 17 , 89 , 63 , 11],
          [75 , 28 , 94 , 36 , 58],
          [7 , 81 , 49 , 22 , 97],
          [65 , 3 , 54 , 39 , 70]]

maior = 0

for linha in range(0 , len(matriz) , 1):

    for coluna in range(0 , len(matriz[linha]) , 1):

        if matriz[linha][coluna] > maior :

            maior = matriz[linha][coluna]

print(maior)
