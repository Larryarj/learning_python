while True:

    acao = int(input('qual ação você quer realizae? \n'
                     '1 para falar com arendente;\n'
                     '2 para reclamar segunda via;\n'
                     '3 para cancelar serviço.\n'))

    match acao:

        case 1:
            print('conectando chamada com atendente...')

        case 2:
            print('imprimindo segunda via...')

        case 3:
            print('cancelando serviço...')

        case _:
            print('opção invalida!')
            break
