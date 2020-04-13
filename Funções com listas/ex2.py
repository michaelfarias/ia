#-----------------------------------------------
def main():
    '''
    Dada uma sequencia de n > 0 numeros inteiros,
    imprimi-la eliminando as repeticoes.
    '''
    n = int(input("Insira a quantidade: "))
    lista = []
    
    while n > 0:
	num = int(input("Numero: "))
	lista.append(num)
	n -= 1

    aux = []
    j = 1
    aux.append(lista[0])
    while j < len(lista):
	contains = False
	for i in range(0, len(aux)):
		if pertence(lista[j], aux):
			contains = True
			break
	if not contains:
		aux.append(lista[j])

	j += 1


    print(aux)
   
#-----------------------------------------------
def pertence(item,lista):
    '''(objeto, list) -> bool

    Recebe uma lista de itens e um item e
    retorna True se o item eh um elemento da lista e
    False em caso contrario.
    '''
    for i in range(0, len(lista)):
	if item == lista[i]:
		return True

    return False

#--------------------------------------------------


def main2():
    n = int(input("Quantidade: "))
    lista = []
    while n > 0:
	lista.append(int(input("Numero: ")))
	n -= 1

    aux = []
    for i in range(0, len(lista)):
	if  lista[i]not in aux:
		auxa.append(lista[i])

    print(aux)

if __name__ == '__main__':
    main()
