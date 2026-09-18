nome = input('digite seu nome completo')

print(f'nome em maiusculo: {nome.upper()}')
print(f'nome em minusculo: {nome.lower()}')

semespaco = nome.replace(' ', '')
print(f'quandidade de letras no nome sem contar espaços: {len(semespaco)}')

separado = nome.split()
print(f'quantidade de letras do primeiro nome: {len(separado[0])}')
