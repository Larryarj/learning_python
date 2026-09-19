cassificacao = input('qual a classificassão do filme? ')

match cassificacao:

    case 'L':
        print('livre para todos os públicos')

    case 10:
        print('proibido para menores de 10 anos')

    case 14:
        print('proibido para menores de 14 anos')

    case 16:
        print('proibido para menores de 16 anos')

    case 18:
        print('proibido para menores de 18 anos')

    case _:
        print('classificação invalida!')
        