numero = 17

while True:
  chute = int(input('chute um numero(inteiro):'))
  if chute == numero:
    print('acertou!')
    break

  elif chute > numero:
    print('chute maior que o numero certo, tente novamente!')

  else:
    print('chute menor que o numero certo, tente novamente!')
