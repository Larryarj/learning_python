infantil = 0
juvenil = 0
junior = 0
adulto = 0

for alunos in range(10):
    nome_aluno = input('qaul o nome no aluno? ')
    idade = int(input('qual a idade do aluno? '))

    if idade < 0:
        print('idade invalida')

    elif idade < 12:
        infantil += 1

    elif idade < 15:
        juvenil += 1

    elif idade < 18:
        junior += 1

    else:
        adulto += 1

print('jogadores infantis: ' , infantil)
print('jogadores juvenis: ' , juvenil)
print('jogadores juniors: ' , junior)
print('jogadores adultos: ' , adulto)
