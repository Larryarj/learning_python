valor_compra = float(input('digite o valor da compra:'))

if valor_compra >= 500:
  desconto = 15
  valor_compra_com_desconto = valor_compra * 0.85
  print(f'valor da compra {valor_compra}, com desconto de {desconto}%: {valor_compra_com_desconto}')

elif valor_compra > 200:
  desconto = 10
  valor_compra_com_desconto = valor_compra * 0.9
  print(f'valor da compra {valor_compra}, com desconto de {desconto}%: {valor_compra_com_desconto}')

else:
  print('sem desconto!')
