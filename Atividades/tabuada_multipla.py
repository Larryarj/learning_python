#67
lista = []

qtd = int(input('digite quantos numeros voce quer ver a tabuada: '))

for i in range(0 , qtd , 1):
    num = int(input('digite um dos numeros que voce quer ver a tabuada: '))
    lista.append(num)

for numero in lista:
    
    for i in range(1 , 10 + 1 , 1):
        
        print(i * numero)
