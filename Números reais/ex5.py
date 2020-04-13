import math

def main():
    x = float(input("Insira x: "))
    epsilon = float(input("valor de epsilon: "))
    s = 0.0
    k = 0
    while  s < epsilon:
	s +=  (x**k) / math.factorial(k)
	k += 1

    print("Aproximacao e^x: ", s)


#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()
