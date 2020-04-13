#-----------------------------------------------
def main():
    '''
    Dados n e uma sequencia com n numeros inteiros,
    conta e imprime o numero de vezes que cada
    numero ocorre na sequencia.
    '''
    n = int(input("Quantidade de elementos: "))
    lista = []
    while n > 0:
        lista.append(int(input("Numero: ")))
        n -= 1
    
    aux = []
    aux.append(lista[0])
    for i in range(1, len(lista)):
        if indice(lista[i], aux) == None:
            aux.append(lista[i])
    
    
    for i in range(0, len(aux)):
        cont = 0
        for j in range(0, len(lista)):
            if aux[i] == lista[j]:
                cont += 1
                
        print("Para ", aux[i], " total de: ", cont)
    
 
#-----------------------------------------------
def indice(item, lista):
    '''(objeto,list) -> int ou None

    Recebe um objeto 'item' e uma lista 'lista' e retorna o
    indice da posicao em que item ocorre na lista.
    Caso item nao ocorra na lista a funcao retorna None
    '''
    for i in range(0, len(lista)):
        if item == lista [i]:
            return i
        
    return None


#-----------------------------------------------
if __name__ == '__main__':
    main()
