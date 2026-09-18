city = input('digite o nome da sua cidade: ')
normalizacao = city.upper()
separado = normalizacao.split()

if 'santo' in city:

    if separado[0] == 'SANTO':
        print('sua cidade começa com santo.')

    else:
        print('sua cidade não começa com santo')

else:
    print('sua cidade não tem santo no nome.')
