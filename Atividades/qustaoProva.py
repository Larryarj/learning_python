idades = []
maiores = []

for i in range(0 , 10 , 1):
    idade = int(input('digite sua idade: '))
    idades.append(idade)

for j in range(0 , len(idades), 1):
    if idades[j] >= 18:
        maiores.append(idades[j])

print(f'maiores: {len(maiores)}')
print(f'media: {sum(idades) / len(idades)}')