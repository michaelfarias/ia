def main():
    a = int(input("valor de a: "))
    b = int(input("valor de b: "))
    c = int(input("valor de c: "))

    if a > b and a > c:
	print(a)
	if b > c:
		print(b)
		print(c)
	else:
		print(c)
		print(b)

    elif a > b and a < c:
	print(c)
	print(a)
	print(b)

    elif b > a and b > c:
	print(b)
	if a > c:
		print(a)
		print(c)
	else:
		print(c)
		print(a)

    elif b > a and b < c:
	print(c)
	print(b)
	print(a)

    else:
	print(c)
	if a > b:
		print(a)
		print(b)
	else:
		print(b)
		print(a)




#-----
if __name__ == '__main__':
    main()
