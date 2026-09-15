dias = int(input('quantos dias o carro foi alugado: '))
kms = float(input('quantos kilometros o carro andou: '))
total = (dias * 60) + (kms * 0.15)

print(f'o total do aluguel foi de {total}')
