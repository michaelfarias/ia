def main():
    num = int(input("Insira um numero diferente de 0: "))
    soma = num
    while num != 0:
    	num = int(input("Insira um numero diferente de 0:"))
	soma += num

    print ("Soma: ", soma)

#-----
if __name__ == '__main__':
    main() 
