def main():
   n = int(input("Insira um numero: "))

   eh_primo = True
   cont = 0

   while n != 0:

	i = 1
	while i < n :

		if (n % i == 0 and i != 1):
			eh_primo = False
		i += 1

	if eh_primo or (n ==1 or n == 2):
		cont += 1

	eh_primo = True

	n = int(input("Insira um numero: "))

   print("Essa sequencia existem ", cont, "numeros primos!")





#--------------------------------------------------
if __name__ == '__main__':
    main()
