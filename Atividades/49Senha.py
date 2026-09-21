senha = '1234'
while True:
    tentativa = input('digite a senha: ')
    if tentativa == senha:
        print('acesso permitido!')
        break
    else:
        print('senha incorreta!')
