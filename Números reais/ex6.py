def main():
    x = float(input("Valor de x: "))
    epsilon = float(input("Valor de epsilon: "))
    
    r_ant = x
    while True:        
        r = (r_ant +(x / r_ant)) / 2.0
       
      
        if abs(r - r_ant) < epsilon:
            break
        
        r_ant = r
       
        
    print(r)

#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()
