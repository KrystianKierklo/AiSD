def foo_z_02(imie, nazwisko):
    imie = imie.capitalize()
    nazwisko = nazwisko.capitalize()
    return imie[0]+". "+nazwisko

def foo(imie, nazwisko, foo_z_02):
    wynik = foo_z_02(imie, nazwisko)
    return wynik

imie = "Krystian"
nazwisko = "kowalski"
print(foo(imie, nazwisko, foo_z_02))
