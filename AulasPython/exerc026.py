frase = input('digite qualquer frase: ')
normalizacao = frase.upper()

print(f'a frase tem: {normalizacao.count('A')} letras a')

print(f'o primeiro a está na posição {normalizacao.find('A') +1}')
print(f'o ultimo a está na posição {normalizacao.rfind('A') +1}')
