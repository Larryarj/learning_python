# crie uma função que recebe um numero e faz um contador regrssivo a partir dele

tempo_cronometro = int(input('quanto tempo voce deseja cronometrar? '))

def cronometro(tempo):
    for i in range(tempo,0,-1):
        print(f'temporizador:{i}')

cronometro(tempo_cronometro)