def main():
    n = int(input("Insira um numero (n > 0): "))
    num = int(input())
    eh_arit = True
    aux = 0
    i = n

    while n-1 > 0:
	num2 = int(input())

	r = num2 - num
	r_ant = num - aux
	aux = num
	num = num2

	if r != r_ant and i != 2:
		eh_arit = False

	n -= 1

    if eh_arit:
	print("Eh uma progressao aritmetica")
    else:
	print("Nao eh!")


#--------------------------------------------------
if __name__ == '__main__':
    main()

