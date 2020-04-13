def main():
    m = int(input("m: "))
    i = 0
    print("Preencha para numeros m:")
    x = []
    while i < m :
        x.append(int(input("Numero m: ")))
        i += 1
    
    y = []
    i = 0
    print("Preencha para numeros n:") 
    n = int(input("n: "))
    while i < n :
        y.append(int(input("Numero n: ")))
        i += 1
    
    j = 1
    k = 1
    aux = x + y
    lista = []
    lista.append(aux[0])
    while j < len(aux):
        contains = False
        for i in range(0, len(lista)):
            if lista[i] == aux[j]:
                contains = True
        
        if not contains:
            lista.append(aux[j])
	    k += 1
            
        j += 1
    
    print("Lista dos m: ", x)
    print("Lista dos n: ", y)
    print("Intercalacao de m e n:", sorted(lista))
#--------------------------------------------------
if __name__ == '__main__':
    main()
