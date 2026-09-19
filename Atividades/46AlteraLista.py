cidades = []

for i in range(0, 4, 1):
    cidade = input('digite o nome da cidade: ')
    cidades.append(cidade)

print(cidades)

atualizacao = input('digite o nome da cidade que vai atualizar: ')
cidades.pop(1)
cidades.insert(1, atualizacao)

print(cidades)
