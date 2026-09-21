nome = input('qual seu nome? ')
idade = int(input('qual sua idade? '))
mf = float(input('qual sua média final? '))
rendaf = float(input('qual sua renda familiar mensal? '))

while True:

    if idade < 16:
        print('Candidato não elegível: idade mínima não atingida.')
        continue

    elif mf >= 9.0 and rendaf <= 2000:
        print('bolsa integral aprovada')
        break

    elif mf >= 8.0 and rendaf <= 3500:
        print('bolsa de 50% aprovada')
        break

    elif mf >=7 and rendaf <= 5000:
        print('bolsa de 25% aprovada')
        break

    else:
        print('candidato não aprovado para bolsa')
        break
