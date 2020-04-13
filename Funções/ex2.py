def main():
    ''' testes da funcao fatorial '''
    print("0! =", fatorial(0))
    print("1! =", fatorial(1))
    print("5! =", fatorial(5))
    print("17! =", fatorial(17))

#-----------------------------------------------------

def fatorial(k):
    #Recebe um inteiro k e retorna o valor de k!
    #Pre-condicaoo: supoe que k é um numero inteiro nao negativo.
    

    k_fat = 1

    # COMPLETE ESSA FUNÇÃO
    
    while k > 0:
        k_fat *= k
        k -= 1


    return k_fat

#-----------------------------------------------------
if __name__ == '__main__':
    main()
