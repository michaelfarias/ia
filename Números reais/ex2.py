def main():
    x = float(input("valor para x: "))
    n = int(input("Primeiros termos da serie: "))
    i = 0
    cos = 0.0

    while i < n:

	fat = 1
	j =  1
	while j <= i*2:
		fat *= j 
		j += 1

	cos += (((-1)**i) * (x**(2*i))) / (fat)

	i += 1

    print("Cos(x) =  ", cos)

#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()
