def main():
    n = int(input("Insira um numero: "))

    adjacente = False

    while n > 0:
	num1 = n % 10
	n = n // 10

	if num1 == n%10:
		adjacente = True

    if adjacente:
	print("sim")
    else:
	print("nao")



#--------------------------------------------------
if __name__ == '__main__':
    main()

