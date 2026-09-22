matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

soma = 0 

for linha in range(0 , len(matriz) , 1):

    for coluna in range(0 , len(matriz[linha]) , 1):
        
        soma += matriz[linha][coluna]

print(f'soma: {soma}')
