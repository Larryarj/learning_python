codigo = input('digite o codigo do produto:\n'
               'a para alimentos não pereciveis\n'
               'v para vestuario\n'
               'e para eletronicos.')

match codigo:
    case 'a':
      print('alimentos não pereciveis')
    case 'v':
      print('vestuario')
    case 'e':
      print('eletronicos')
    case _:
      print('código invalido!')