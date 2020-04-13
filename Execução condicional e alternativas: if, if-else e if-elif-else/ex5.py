def main():

    a = int(input("valor de a: "))
    b = int(input("valor de b: "))
    c = int(input("valor de c: "))

    if pow(a,2) == (pow(b, 2) + pow(c, 2)):
	print("Forma um triangulo retangulo")
    else:
	print("Nao eh triangulo retangulo")



#-----
if __name__ == '__main__':
    main()

