def main():
    n = int(input("Insira um numero: (n > 0)"))
 
    h_n = 0.0
    i = 1.0
    while i <= n:

	h_n += 1.0/i
	i += 1.0

    print("H_n crescente: ", h_n)

    i = n
    h_n = 0.0
    while i > 0:
	h_n += 1.0 / i
	i -= 1

    print("H_n decrescente: ", h_n)


#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()
