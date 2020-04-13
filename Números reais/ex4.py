def main():
    x = float(input("Coordenada x: "))
    y = float(input("Coordenada y: "))
    
    if 1 <= y <= 2 and  -3 <= x <= 3:
        print("dentro")
        
    elif (4 <= y <= 5  or  6 <= x <= 7) and ( -4 <= x <= -3 or -2 <= x <= -1 or  1 <= x <= 2 or  3 <= x <= 4):
        print("dentro")
   
    else:
        print("fora")



#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()
