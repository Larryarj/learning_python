alcance = int(input('digite até que numero da sequencia fibonacci voce quer ver: '))
n1 = 0
n2 = 1
print(n1)
print(n2)
for numero in range(0 , alcance , 1):
    sequencia = n1 + n2
    n1 = n2
    n2 = sequencia
    print(sequencia)
