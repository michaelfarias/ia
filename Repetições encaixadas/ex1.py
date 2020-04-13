def main():
    n = int(input("Numero: "))

    j = 2
    while n != 1:
	eh_primo = True
	i = 2

	while(i < j ):
		if j % i == 0:
			eh_primo = False
		i +=1
	if eh_primo:
		if n%j == 0:
			cont = 0
			while n%j == 0:
				n /= j
				cont += 1

			print ("fator ", j,"multiplicidade ", cont )

	j += 1


#--------------------------------------------------
if __name__ == '__main__':
    main()
