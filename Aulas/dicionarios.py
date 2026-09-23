# aula vinicius
"""endereco
numero, rua, bairro, cidade, cep, estado
"""

endereco = {
    'num' : "SN",
    'rua' : "Alfredo Lustosa Cabral",
    'bairro' : "Salgadinho",
    'cidade' : "Patos",
    'cep' : 57806550,
    'estado' : "Paraíba"
}

# for chave, valores in endereco.items():
#     print(chave, valores)
# for i in endereco.keys():
#     print(i, endereco[i])

boletim = {
    'Matemática': 0,
    'Português': 0,
    'Ciências': 0,
    'História': 0,
    'Geografia': 0
}

boletim['Inglês'] = 1 #adiciona elemento
boletim.update({'Aritmética': 0}) #adiciona elemento

boletim.pop('Matemática') #Remove Elemento

boletim['História'] = 10 # Altera valor de elemento
boletim.update({'Geografia': 10}) # Altera valor de elemento

print(boletim)

for chave, valor in boletim.items():
    
    print(f"Digite a nota de {chave}")
    boletim[chave] = float(input(" "))

for chave, valor in boletim.items():
    
    if valor == min(boletim.values()):
        print(f"Menor nota foi em {chave}")
    
    elif valor == max(boletim.values()):
        print(f"A matéria com maior nota é {chave}")

print("A média é ", sum(boletim.values())/len(boletim.values()))
