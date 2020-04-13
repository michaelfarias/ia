def main():
    n = int(input("Insira um numero: "))

    i = 1 

    eh_primo = True

    while i < n:
	if n % i == 0 and i != 1:
		eh_primo = False
	i += 1

    if eh_primo:
	print("Eh primo")
    else:
	print("Nao eh primo")

#-----
if __name__ == '__main__':
    main()
