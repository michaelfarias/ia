import math
def main():
    # Escreva o seu programa
    n = int(input("Valor de n: "))
    m = int(input("Valor de m(m>=n): "))
    
    print(math.factorial(m) / (math.factorial(m - n) * math.factorial(n)))


#-----------------------------------------------------
if __name__ == '__main__':
    main()
