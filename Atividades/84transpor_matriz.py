matriz = [[42 , 17 , 89 , 63],
          [75 , 28 , 94 , 36],
          [7 , 81 , 49 , 22],
          [65 , 3 , 54 , 39]]

for linha in range(0 , len(matriz) , 1):
    print(matriz[linha])

print('-'*30)

transposta = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

# tentando inverter indices da matriz(linhas em colunas e colunas em linhas)

for linha in range(0 , len(matriz) , 1):

    for coluna in range(0 , len(matriz[linha]) , 1):

        transposta[coluna][linha] = matriz[linha][coluna] 

for linha in transposta:

    print(linha)

#linhas = len(matriz)
#colunas = len(matriz[0])

#transposta = [[0] * linhas for _ in range(colunas)]   # "Crie uma lista com (colunas) linhas, e em cada linha coloque uma lista com (linhas) zeros."

#for i in range(linhas):
    #for j in range(colunas):
        #transposta[j][i] = matriz[i][j]

#print(transposta)
