liczba = 0
suma = 0

while True:
    liczba=int(input("Podaj liczbe: "))
    suma = suma + liczba
    if suma >= 100:
        print("Suma liczb przekroczyla 100 :)")
        break