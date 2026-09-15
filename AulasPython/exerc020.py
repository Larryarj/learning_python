import random
alunos = []

for i in range(0, 4, 1):
    al = input(f'digite o nome do {i +1} aluno: ')
    alunos.append(al)

random.shuffle(alunos)
print(alunos)
