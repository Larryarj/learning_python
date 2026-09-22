# crie um código que calcule a area de um cilindro

altura_cil = float(input('qual a altura do cilindro? '))
raio_cil = float(input('qual o raio do cilindro? '))
PI = 3.14

def calcular_vol_cil(altura,raio):
    
    volume_cil = PI * (raio**2) * altura

    print(volume_cil)

calcular_vol_cil(altura_cil,raio_cil)
