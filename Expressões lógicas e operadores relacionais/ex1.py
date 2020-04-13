def main():
    num = int(input("Insira numero: "))
    print("Eh bissexto?", ((num%4 == 0) and  not (num%100 == 0)) or ((num%4 == 0) and  (num%100 == 0) and ( num%400 == 0)))



    # Fim do programa

#-------------------------------------------
if __name__ == '__main__':
    main()
