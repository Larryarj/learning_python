nomes = [['ana' , 'bruno' , 'carlo' , 'daniel' , 'edu'],
         ['1' , '2' , '3' , '4' , '5']]

puxar_nome = input('qual none vc quer puxar da lista? ')

if puxar_nome in nomes[0]:
    
    nome_index = nomes[0].index(puxar_nome)

    print('nome encontrado. índice:', nome_index)

