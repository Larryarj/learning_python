def encontrar_num(lista, indice , num):
    
    if indice >= len(lista):
        return lista[indice -1]
    
    if lista[indice] != num:
        encontrar_num(lista , indice + 1 , num)

    else:
        print('não encontrado!')
        return num

def main ():
    
    numeros = [1,2,3,4,5,6,7,8,9]
    num_certo = 8
    print(f'encontrado {num_certo}')

main()
