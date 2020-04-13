def main():
    n = int(input("Insira n: "))
    k = int(input("Insira k: "))
    exp = 1

    while k > 0:
	exp *= n
	k = k - 1

    print("valor de n^k: ", exp)


if __name__ == '__main__':
    main() # chamada que inicia o programa
