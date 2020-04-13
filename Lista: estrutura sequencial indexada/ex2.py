def main():
    n = int(input("Insira um numero: "))
    l = []
    
    while n > 0:
        num = float(input("Numero: "))
        l.append(num)
        n -= 1
    
    j = 1
    k = 0
    aux = []
    aux.append(l[0])
    
    while j < len(l):
        contains = False
        
        for i in range (0, len(aux)):
            if aux[i] == l[j]:
                contains = True
                
        if not contains:
            aux.append(l[j])
            k += 1
        
        j += 1
           
        
    print("Lista com repetidos: ", l)
    print("Lista sem repetidos: ", aux)

#--------------------------------------------------
if __name__ == '__main__':
    main()
