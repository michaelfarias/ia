def main():
    num = int(input("Insira um numero: "))
    fat = 1

    while num > 0:
	fat *= num
	num -= 1

    print ("fatorial: ", fat)

#-----
if __name__ == '__main__':
    main() # chamada que inicia o programa

