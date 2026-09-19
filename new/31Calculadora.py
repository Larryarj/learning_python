num1 = int(input('digite um numero inteiro:'))
num2 = int(input('digite um numero inteiro:'))
op = input('digite a operacao (+, -, *, /):')

if op == '+':
    resultado = num1 + num2

elif op == '-':
    resultado = num1 - num2

elif op == '*':
    resultado = num1 * num2

elif op == '/':
    resultado = num1 / num2

else:
   print('operacao invalida!')

print(f'resultado: {resultado}')
