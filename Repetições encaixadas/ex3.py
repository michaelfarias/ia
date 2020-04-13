def main():
    n = int(input("Insira um numero: "))

    while n > 0:
	num = int(input("Numero: "))
	fat = 1
	while num > 0:
		fat *= num
		num -= 1

	print("Seu fatorial eh: ", fat)

	n -= 1

#--------------------------------------------------
if __name__ == '__main__':
    main()
