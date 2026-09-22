# como imprimir respectivamente as variaveis de uma matriz que estao em linhas diferentea

matriz_bancodados = [['ana','bruno','carlo','daniel','edu'],
                     [20 , 23, 25, 22, 24]]

for pessoa in range(0 , len(matriz_bancodados[0]), 1):
    
    print(matriz_bancodados[0][pessoa] , matriz_bancodados[1][pessoa])
