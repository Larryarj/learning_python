quantia = int(input('digite o valor do saque:'))

if (quantia % 2) == 0:

  notas_cem = quantia // 100
  resto_cem = quantia % 100

  notas_cinquenta = resto_cem // 50
  resto_cinquenta = resto_cem % 50

  notas_vinte = resto_cinquenta // 20
  resto_vinte = resto_cinquenta % 20

  notas_dez = resto_vinte // 10
  resto_dez = resto_vinte % 10

  notas_cinco = resto_dez // 5
  resto_cinco = resto_dez % 5

  notas_dois = resto_cinco // 2
  resto_dois = resto_cinco % 2



  print(f'Notas de R$100: {notas_cem}')
  print(f'Notas de R$50: {notas_cinquenta}')
  print(f'Notas de R$20: {notas_vinte}')
  print(f'Notas de R$10: {notas_dez}')

else:
    print('erro!')
