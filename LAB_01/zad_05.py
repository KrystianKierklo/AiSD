def foo(a, b):
    if (a>0) & (b>0) & (b!=0):
        return a/b
    return "Podano nieprawidlowe wartosci!"

a = int(input("Podaj pierwsza liczbe dodatnia: "))
b = int(input("Podaj druga liczbe dodatnia: "))

print("Wynik dzielenia tych liczb to: ", foo(a,b))