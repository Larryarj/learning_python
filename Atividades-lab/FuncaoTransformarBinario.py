def transformarBinario(decimal):

    binario = []

    while decimal > 0:

        if decimal > 1:

            resto = decimal % 2
            binario.insert(0 , resto)
            decimal = decimal // 2

        else: 
            binario.insert(0 , 1)
            decimal = 0

    return binario

def main():

    numero = int(input('digite um numero para transformar em binário: '))
    print(f'{numero} em binário: {transformarBinario(numero)}')

main()
