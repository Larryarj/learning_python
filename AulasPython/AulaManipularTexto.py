# fatiamento

texto = 'curso em video python'

print('indice 9: ' , texto[9])
print('indice 9 até 14: ' , texto[9:14])
print('indice 9 até 21: ' , texto[9:21])
print('do começo até o indice 5: ' , texto[:5])
print('do indice 15 até o final: ' , texto[15:])
print('do indice 9 até o final, pulando de 3 em 3: ' , texto[9::3])

print('ANALISE')# análise

print('tamanho do texto: ' , len(texto)) # retorna o tamanho da string
print('contando a letra "o": ' , texto.count('o')) # conta quantas vezes alguma coisa aparece
print('contando a letra "o" do indice 0 ao 13: ' , texto.count('o', 0, 13)) # conta quantas vezes alguma coisa aparece com indices
print('encontrando "deo" no texto: ' , texto.find('deo')) # encontra algo no texto
print('encontrando palavra que não existe no texto: ' , texto.find('android')) # encontra algo no texto
print('curso' in texto) # operedor (in), verifica se está dentro do texto, retorna true ou false
print(texto.replace('python' , 'android')) # troca o segundo item pelo primeiro
print(texto.upper()) # coloca tudo em maiusculo
print(texto.lower()) # transforma tudo em minusculo
print(texto.capitalize()) # coloca tudo em minusculo, mas deixa a primeira letra em maiusculo
print(texto.title()) # transforma todas as letras iniciais em maiusculas

print('DIVISAO')# divisão

textosplit = texto.split()
print(texto.split())
print('-'.join(textosplit))

print('ESPAÇOS') # tratando espaços

texto2 = '  aprenda python  '

print(texto2.strip()) # remove espaços inuteis nas extremidades da string
print(texto2.rstrip()) # right strip: remove os espaços a direita
print(texto2.lstrip()) # left strip: remove os espaços a esquerda
