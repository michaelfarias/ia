def main():
    n = int(input("Quantidade: "))
    cont_par = 0
    cont_impar = 0
    while n > 0:
        num = int(input())

        if num %2 == 0:
                cont_par += 1
        else:
		cont_impar += 1

	n -= 1

    print("Quantidade de pares: ", cont_par)
    print("Quantidade de impares: ", cont_impar)

#-----
if __name__ == '__main__':
    main()


