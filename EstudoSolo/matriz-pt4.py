# como printar variaveis de uma linha numa matriz no menso indice de outra linha

bancodedados = [[1,1,2,2,1],
                ['ze','jose','seu ze','rosé','zezin']]

consulta = int(input('qual tipo vc quer consultar? 1 ou 2. '))

for tipo in range(0, len(bancodedados[0]), 1):
    
    if bancodedados[0][tipo] == consulta:
        
        print(f'tipo {consulta}: {bancodedados[1][tipo]}')
