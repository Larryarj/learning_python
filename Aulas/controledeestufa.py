# uma estufa precisa do controle de temperatura diario, sendo assim o usuario mede e registra a temperatura no sistema 3 vezes
# ao dia. a temperatura ideal é quando a media das tres medidas fica entre 25 e 28 graus. abaixo disso o dia foi muito frio,
# acima, muito quente. 
# o programa deve reveber 3 medidas por dia e retornar quantos graus a estufa deve ajustar para que a 
# temperatura media continue ideal. 
# o funcionario dirá quantos dias ele quer registrar
# ao final do programa diga:
# temperatura media de cada dia, se foi frio, quente ou ideal 
# menor e maior temperatura registrada 
# quais dias não foram ideais

#criando variaveis

dias = int(input('quantos dias vão ser registrados? '))
medias = []

diafrio = 0
diaquente = 0
diaideal =0 

# criando loop para receber 

for dia in range(dias):

    #recebendo inputs

    tmanha = float(input('qual a tempratura da manha? '))
    ttarde = float(input('qual a tempratura da tarde? '))
    tnoite = float(input('qual a tempratura da noite? '))

    #calculando medias

    mediadia = (tmanha + ttarde + tnoite) / 3

    #classificando temperaturas

    if mediadia < 25:
        medias.append (mediadia)
        diafrio += 1
        ajuste = 25 - mediadia
        print('aumente a temperatura em pelo menos' , ajuste , 'graus')

    elif mediadia > 28:
        medias.append (mediadia)
        diaquente += 1
        ajuste = mediadia - 28
        print('diminua a temperatura em pelo menos' , ajuste , 'graus')

    else:
        medias.append (mediadia)
        diaideal += 1
        print('hoje o dia foi ideal')

# cauculando resultados

minimo = min(medias)
maximo = max(medias)

# printando tudo

for dia in range(len(medias)):

    print ('a temperatura do dia' , dia , medias[dia], 'graus')

print('a temperatura minima foi: ' , minimo)
print('a temperatura maxima foi: ' , maximo)
