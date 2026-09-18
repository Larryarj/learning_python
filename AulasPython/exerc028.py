import random

print('vou pensar um numero de 0 a 5, tente acertar')

numeros = [1,2,3,4,5]

chute = int(input('digite um numero de 0 a 5: '))

print("você acertou" if chute == random.choice(numeros) else f"você errou, o numero sorteado foi {random.choice(numeros)}")
