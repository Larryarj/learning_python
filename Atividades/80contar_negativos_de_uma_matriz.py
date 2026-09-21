matriz = [[1 , -2 , 3 , -4],
          [5 , -6 , 7 , -8],
          [9 , -10 , 11 , -12],
          [13 , -14 , 15 , -16]]

lista_de_negativos = []
negativos = 0

for linha in range(0 , len(matriz) , 1): #esse for caminha por todas as linhas

    for coluna in range(0 , len(matriz[linha]) , 1): # esse for percorre a linha em que o loop do for anerior estiver passando

        if matriz[linha][coluna] < 0: # esse if verifica se a variavel no índice (linha e coluna) em que os loops estão passando atualmente é menor que zero.
            
            lista_de_negativos.append(matriz[linha][coluna])
            negativos += 1

print(f'quantidade de negativos: {negativos}; Sendo eles: {lista_de_negativos}')
