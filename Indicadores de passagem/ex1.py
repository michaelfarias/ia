def main():
    n = int(input("Insira um numero: "))
    eh_par = True

    while n > 0:
	num = int(input(""))
	if not num%2 == 0:
		eh_par = False
	n -= 1

    if eh_par:
	print("Toda a sequencia eh par")
    else:
	print("A sequencia nao eh par")


#-----
if __name__ == '__main__':
    main()
