kms = float(input('digite quantos quilometros tem sua viagem: '))

if kms <= 200:
    preco = kms * 0.50

else:
    preco = kms * 0.45

print(f"preço da viagem: {preco:.2f}")
