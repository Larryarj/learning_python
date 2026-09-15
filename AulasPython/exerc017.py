import math

catetoopt = float(input('digite o temanho do cateto oposto do triangulo: '))
catetoadj = float(input('digite o temanho do cateto adjacente do triangulo: '))
hipot = math.sqrt((catetoopt ** 2) + (catetoadj ** 2))

print(f'comprimento da hipotenusa: {(hipot):.2f}')

#ou

hip = math.hypot(catetoopt , catetoadj)
print(f'comprimento da hipotenusa: {(hip):.2f}')
