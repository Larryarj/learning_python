salario_bruto = float(input('digite o salario bruto:'))

if salario_bruto <= 2259.20:
    print('isento')

elif salario_bruto <= 2826.65:
    aliquota = 7.5
    salario_liquido = salario_bruto * 0.925
    print(f'salario liquido: {salario_liquido}')

elif salario_bruto <= 3751.05:
    aliquota = 15
    salario_liquido = salario_bruto * 0.85
    print(f'salario liquido: {salario_liquido}')

elif salario_bruto <= 4664.68:
    aliquota = 22.5
    salario_liquido = salario_bruto * 0.775
    print(f'salario liquido: {salario_liquido}')

else:
    aliquota = 27.5
    salario_liquido = salario_bruto * 0.725
    print(f'salario liquido: {salario_liquido}')
    