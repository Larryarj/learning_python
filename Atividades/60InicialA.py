lista = []
qtd = int(input('digite quantos nomes voce quer comparar: '))

for i in range(0, qtd , 1):
    nome = input('digite um nome: ')
    lista.append(nome)

print(lista)

for nome in lista:

    if nome[0] == 'a' or nome[0] == 'A':

        print(nome)
        