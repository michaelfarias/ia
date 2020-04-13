def main():
    n = int(input("Tamanho da sequencia: "))
    list = []
    while n > 0:
	num = float(input("Numero: "))
	list.append(num)
	n -= 1

    soma = 0.0
    soma_aux = 0.0
    soma_ant = 0.0
    start = 0
    end = 0
    s= 0
    e = 0
    for i in range(0, len(list)):
	for k in range(i, len(list)):
		soma_aux += list[k]
		if soma < soma_aux:
			soma = soma_aux
			start = i
			end = k
	soma_aux = 0.0
	if soma > soma_ant:
		soma_ant = soma
		s = start
		e = end

	soma = 0.0

    print(list[s:e + 1]," = ", soma_ant)


#--------------------------------------------------
if __name__ == '__main__':
    main()
