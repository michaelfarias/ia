def main():
    # dados da Penny
    nome = "Penny"
    sexo = "feminino"
    altura = 167
    peso   =  52
    idade  =  25
    cabelo = "loiro"
    escolaridade = "medio"



    compativel = sexo == 'feminino' and  (peso >= 45 and peso <= 65) and  (altura >= 155 and altura <= 170) and (25 <= idade <= 35) and cabelo == "loiro" and not escolaridade == "PhD"

    print("Candidata", nome, ":", compativel)



    # Fim do programa

#-------------------------------------------
if __name__ == '__main__':
    main()

