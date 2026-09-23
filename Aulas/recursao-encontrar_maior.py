def encontrar_maior(lista, index):

    if index >= len(lista): # mecanismo de parada: quando o indice for maior que o tamanho da lista, retorna 0
        return lista[index -1]
    
    maior = encontrar_maior(lista, index +1) #Descida da recursão: ela vai chamando a si mesma até passar do último índice (index == len(lista)), sem fazer comparações.
    
    # Subida da recursão: cada chamada recebe o maior valor encontrado nos índices seguintes e compara esse valor com o elemento da posição atual.
    # Assim, o maior valor "vai sendo carregado" de volta até a primeira chamada, que retorna o maior elemento da lista
    
    if lista[index] > maior:
        return lista[index]
    
    else:
        return maior

def main():

    numeros = [99,43,56,73,24,53,41,34]
    print(f'o maior: {encontrar_maior(numeros, 0)}')

main()
