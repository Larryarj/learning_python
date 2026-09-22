somadasnotas = 500
alunos = 100

vendas = 20.000
vendedores = 7


def f_calculo_media(total,quantidade):
    media = total / quantidade
    return(media)

medianotas = f_calculo_media(somadasnotas,alunos)
#mediavendas = f_calculo_media(vendas,vendedores)

print(medianotas)
print(f_calculo_media(vendas,vendedores))
