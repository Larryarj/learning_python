while True:

    nivel_de_gravidade = int(input('o paciente tem sintomas graves? digite:\\n'
                                    '1 para sim;\n'
                                    '2 para não'))

    if nivel_de_gravidade == 1:

        faixa_etaria = int(input('o paciente pertence ao grupo de risco? (gestante ou idosos). digite:\n'
                                  '1 para sim;\n'
                                  '2 para não'))

        if faixa_etaria == 1:
            print('prioridade vermelha!')

        else:
            print('prioridade amarela')

    else:
        print('prioridade verde!')

    break
