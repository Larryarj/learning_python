quantia = int(input("quantos produtos você vai comprar? ")) 
soma = 0
for i in range (quantia): 
    soma += float(input("Valor do produto: ")) 
    print('o valor atual da compra é:' , soma)
