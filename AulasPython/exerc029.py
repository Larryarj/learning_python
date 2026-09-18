import random
velocidade = random.randint(50, 100)

if velocidade > 80:

    multa = (velocidade - 80) * 7
    print(f"você foi multado por ultrapassar o limite de velocidade, sua velocidade: {velocidade}\n"
          f"sua multa foi de {multa} reais.")

else:
    print(f"sua velocidade: {velocidade}")
