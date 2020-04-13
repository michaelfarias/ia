def main():
    n = int(input("Insira um numero: "))
    i = 0
    t = (i + 1) * (i + 2) * (i + 3)
    while t < n:
	i += 1
        t = (i + 1) * (i + 2) * (i + 3)

    if t == n:
	print("O numero eh triangular")
    else:
	print("Nao eh triangular")



#-----
if __name__ == '__main__':
    main()
