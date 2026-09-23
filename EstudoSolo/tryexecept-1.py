#               ========== tratamento de exceção com try e except ===========


# exemplo 1 : tratamento de erro geral ===================================================



# try:
#     n1 = int(input('digite um número inteiro: '))
#     n2 = int(input('digite outro número inteiro: '))
#     resultado = n1 + n2

#     print(f'o resultado da soma de {n1} + {n2} é: {resultado}')

# except:
#     print('ocorreu um erro, digite apenas números inteiros. Ex: 1, 2, 3...')


# exemplo 1.2: =============


try:
    n1 = int(input('digite um número inteiro: '))
    n2 = int(input('digite outro número inteiro: '))
    resultado = n1 + n2

    print(f'o resultado da soma de {n1} + {n2} é: {resultado}')

except Exception as error:
    print(f'ocorreu um erro: {error}')



# exemplo 2 : tratamento de erro específico ====================================================



# try:
#     nu1 = int(input('digite um número inteiro: '))
#     nu2 = int(input('digite outro número inteiro: '))
#     resultado2 = nu1 + nu2

#     print(f'o resultado da soma de {nu1} + {nu2} é: {resultado2}')

# except ValueError as error:
#     print(f"erro ocorrido: {error}")


# exemplo 2.2 :=================


# try:
#     nume = int(input('digite um número inteiro: '))
#     result = 10 / nume

#     print(f'o resultado da divisão de 10 / {nume} é: {result}')

# except ValueError as error:
#     print(f"erro: {error}")

# except ZeroDivisionError as error:
#     print(f"erro: {error}")


# exemplo 2.3 :=================

# try:
#     lista = ['uva', 'banana', 'laranja']
#     print(lista[4])

# except IndexError as error:
#     print(f"erro: {error}")



# exemplo 3 : tratamento de múltiplos erros ====================================================



# try:
#     num1 = int(input('digite um número inteiro: '))
#     num2 = int(input('digite outro número inteiro: '))
#     resultado3 = num1 + num2

# except ValueError as error:
#     print(f"erro de valor ocorrido: {error}")

# except TypeError as error:
#     print(f"erro de tipo ocorrido: {error}")

# else:
#     print(f'o resultado da soma de {num1} + {num2} é: {resultado3}')



# exemplo 4 : tratamento de múltiplos erros com else e finally ====================================================



# try: 
#     numero1 = int(input('digite um número inteiro: '))
#     result = 10 / numero1
    
# except ValueError as error:
#     print(f"erro de valor ocorrido: {error}")

# except ZeroDivisionError as error:
#     print(f"erro de divisão por zero ocorrido: {error}")

# except TypeError as error:
#     print(f"erro de tipo ocorrido: {error}")

# else:
#     print(f"10 dividido por {numero1} é: {result}")

# finally:
#     print("bloco finally executado")
