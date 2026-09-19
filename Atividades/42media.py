lista = []

for i in range(0, 4 , 1):
    nota = float(input((f'digite a {i+1} nota do aluno: ')))
    lista.append(nota)

media = (lista[0] + lista[1] + lista[2] + lista [3]) / 4

print(f'media: {media}')
