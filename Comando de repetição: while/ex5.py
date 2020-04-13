def main():
    a = int(input("insira a: "))
    b = int(input("insira b: "))

    while b != 0:
	r = b
	b = a % b
	a = r

    print (a)




#-----
if __name__ == '__main__':
    main() # chamada que inicia o programa

