def main():
    ''' Testes da funcao combincao '''
    print("Combinacao(4,2) =", combinacao(4,2))
    print("Combinacao(5,2) =", combinacao(5,2))
    print("Combinacao(10,4) =", combinacao(10,4))

#-----------------------------------------------------

def combinacao(m, n):
    '''(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    '''

    # COMPLETE ESSA FUNÇÃO E MUDE O RETURN ABAIXO

    return fatorial(m) / (fatorial(m - n) * fatorial(n))

#-----------------------------------------------------

def fatorial(k):
    k_fat = 1
    while k > 0:
        k_fat *= k
        k -= 1


    return k_fat
#------------------------------------------------------
if __name__ == '__main__':
    main()
