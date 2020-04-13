#-----------------------------------------------
def main():
    """
    programa que calcula segmento de soma maxima
    """
    n = int(input("Tamanho da sequencia: "))
    lista = []
    while n > 0:
        lista.append(float(input("Numero: ")))
        n -= 1
    
    start = 0
    end = 0
    soma_ant = 0.0
    for i in range(0, len(lista)):
        for j in range(i, len(lista)):
            soma = soma_elementos(i, j + 1, lista)
            if soma > soma_ant:
                soma_ant = soma
                start = i
                end = j
     
    print(lista[start: end + 1]," = ", soma_ant)
            
    
def soma_elementos(ini, fim, lista):
    
    soma = 0
    for i in range(ini, fim):
        soma += lista[ i ]
        
    return soma
#-----------------------------------------------
if __name__ == '__main__':
    main()
