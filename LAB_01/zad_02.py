def foo(imie, nazwisko):
    imie = imie.capitalize()
    nazwisko = nazwisko.capitalize()
    return imie[0]+". "+nazwisko

print("Podaj imie: ")
imie = input()
print("Podaj naziwsko: ")
nazwisko = input()

print(foo(imie, nazwisko))