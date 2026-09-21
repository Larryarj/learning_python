nome = input('digite seu nome: ')

print(f'bem vindo a análise de crédito  {nome}!')

pontuacao = 0

while True:

    restricao = int(input('voce possui restrição no seu nome? digite:\n'
                          '1 para sim;\n'
                          '2 para não.'))

    if restricao == 1:
        pontuacao += 1

    else:
      pass

    salario = float(input('qual sua renda mensal? '))

    if salario < 2000:
        pass

    elif salario > 2000 and salario < 5000:
        pontuacao += 1

    else:
        pontuacao += 2

    tempo_emprego = int(input('voce já tem mais de um ano de emprego? digite:\n'
                              '1 para sim;\n'
                              '2 para não.'))

    if tempo_emprego == 1:
        pontuacao += 1

    else:
        pass

    break

if pontuacao <= 1:
    print('crédito recusado.')

elif pontuacao == 2 or pontuacao == 3:
    print('crédito aprovado com baixo limite.')

else:
    print('crédito aprovado com alto limite.')
    