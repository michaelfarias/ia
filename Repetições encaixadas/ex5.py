def main():
    n =  int(input("Insira um numero"))
    i = 1
    s = 0
    aux = 1
    cons = i
    while s != n ** 3:
	j = 0
	s = 0
 	aux = i
	while j < n:
		s += i
		i += 2
		j += 1
	cons = i - 2
	i = aux + 2

    st = ""
    while n > 0:
	st += " " +str(cons)
	cons -= 2
	n -= 1

    print (st)


#--------------------------------------------------
if __name__ == '__main__':
    main()
