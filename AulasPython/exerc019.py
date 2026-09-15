import random
alunos = []

for i in range(0 , 4, 1):
    aluno = input(f'digite o nome do {i +1} aluno: ')
    alunos.append(aluno)

sorteado = random.choice(alunos)
print(f'sorteado: {sorteado}')
