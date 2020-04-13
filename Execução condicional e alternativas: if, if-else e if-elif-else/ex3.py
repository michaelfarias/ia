def main():
    n = int(input("Digite o valor de n (n >0): "))
    d = int(input("Digite o valor de d (0<=d<=9): "))

    cont = 0

    while n > 0:
	r = n%10
	n = n // 10

	if r == d:
		cont += 1

    print("O digito ", d, " ocorreu ", cont, " vezes")



#-----
if __name__ == '__main__':
    main()
