num1 = int(input('digite o primeiro numero:'))
num2 = int(input('digite o segundo numero:'))
op = input('digite a operacao (+, -, x, /):')

match op:
    case '+':
        result = num1 + num2
        print(f'resultado: {result}')
    case '-':
        result = num1 - num2
        print(f'resultado: {result}')
    case 'x':
        result = num1 * num2
        print(f'resultado: {result}')
    case '/':
        result = num1 / num2
        print(f'resultado: {result}')
        