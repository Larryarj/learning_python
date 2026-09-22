#66
usuario = input('defina o nome do usuário da sua conta: ')
senha = input('defina a senha da sua conta: ')
pin = input('defina seu pin: ')

login = int(input('deseja fazer login? digite:\n'
                  '1 para sim;\n'
                  '2 para não.'))

if login == 1:

    while True:
        tentativa_usuario = input('digite o nome do usuário: ')
        tentativa_senha = input('digite a senha: ')

        if tentativa_usuario == usuario and tentativa_senha == senha:
            print('usuário reconhecido.')

            while True:
                tentativa_pin = input('digite o pin: ')

                if tentativa_pin == pin:
                    print('acesso permitido!')
                    break

                else:
                    print('acesso negado, pin incorreto!')

            break

        else:
            print('acesso negado! usuário ou senha incorreto!')

else:
    print('até numca mais...')
