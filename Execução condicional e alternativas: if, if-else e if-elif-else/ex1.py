def main():
    n = int(input("Quantidade: "))
    soma = 0
    while n > 0:
	num = int(input())

	if num %2 == 0:
		soma += num
	n -= 1

    print("Soma dos pares: ", soma)


#-----
if __name__ == '__main__':
    main()
