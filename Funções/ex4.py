# Escreva o seu programa usando o esqueleto sugerido

def combinacao(m, n):

    return fatorial(m) / (fatorial(m - n) * fatorial(n))

#-----------------------------------------------------

def fatorial(k):
    k_fat = 1
    while k > 0:
        k_fat *= k
        k -= 1


    return k_fat
#------------------------------------------------------

def main():
    n = int(input("Numero: "))

    k = 0
   
    while k <= n :
	c = combinacao(n, k)

        print c,"x^",(n - k),"y^",k
	k += 1
    
    
#-----------------------------------------------------
if __name__ == '__main__':
    main()
