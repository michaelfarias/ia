def main():
   x = float(input("Valor para x: "))
   e = float(input("Valor para e: "))

   s = 0.0
   i = 0

   while  abs(s) < e:

	fat = 1
	j = 1

	while j <= (2 * i + 1):
		fat *= j
		j += 1

	s += float(((-1)**i) *( (x**(2*i + 1)) / fat))

	i += 1

   print("Valor aproximado para sin(x): ", s)
#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()

