def main():
    n = int(input("Insira um numero (n > 0): "))

    num = int(input("Numero: "))

    while n - 1 > 0:
	num2 = int(input("Numero: "))


	while num2 > 0:
		r = num%num2
		num = num2
		num2 = r



	n -= 1

    print("MDC - ", num)

#--------------------------------------------------
if __name__ == '__main__':
    main()
