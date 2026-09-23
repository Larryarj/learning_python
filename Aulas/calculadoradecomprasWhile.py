quantia = int(input('quantos produtos vão ser comprados?'))
i = 0
soma = 0
while i < quantia:
    i += 1
    aux = float(input('qual o preço do produto?'))
    print('o produto custa' , aux , 'reis')
    soma = soma + aux 
    print('o valor atual da compra é de' , soma , 'reais')

print('o valor total é: ' , soma)
