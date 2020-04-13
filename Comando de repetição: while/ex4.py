def main():
    n = int(input("valor de n: "))
    i = int(input("valor de i: "))
    j = int(input("valor de j: "))

    aux = 0


    while i < j and aux < n :

	print(j * aux)

	aux += 1

	print(i*aux)


    while i > j and aux < n/2:
	print(i * aux)

	aux += 1
	print(j*aux)
#-----
if __name__ == '__main__':
    main() # chamada que inicia o programa

