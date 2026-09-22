valor_compra = float(input('qual o valor da sua compra? '))

if valor_compra >= 500:
    desconto = float(valor_compra * 0.20)
    valor_final = valor_compra * 0.80

elif valor_compra >= 200:
    desconto = float(valor_compra * 0.10)
    valor_final = valor_compra * 0.90

elif valor_compra >= 100:
    desconto = float(valor_compra * 0.05)
    valor_final = valor_compra * 0.95

else:
    print('o valor atual da compra não recebe desconto.')

print('o desconto foi de: ' , desconto)
print('o valor final com desconto foi de: ' , valor_final)
