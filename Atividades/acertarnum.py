numero = 7
chute = int(input('chute um numero '))
while chute != numero:
    if chute > numero:
        print('numero muito alto, tente novamente ')

    else :
        print('numero muito baixo, tente novamente ') 
    
    chute = int(input('chute novamnete '))

print('voce acertou, o numero é: ' , numero)
