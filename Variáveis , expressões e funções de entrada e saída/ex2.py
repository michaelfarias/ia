#fahrenheit to celsius
def main():
    fahrenheit = float(input("Digite a temperatura: "))
    celsius =  (fahrenheit - 32.0)*5.0/9.0

    print("Celsius: ", celsius)
    # Fim do Programa


if __name__ == '__main__':
    main() # chamada que inicia o programa
