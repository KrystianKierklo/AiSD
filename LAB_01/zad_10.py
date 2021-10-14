def foo(wyraz):
    dlugosc = len(wyraz)
    while dlugosc:
        dlugosc = dlugosc - 1
        if wyraz[dlugosc] != wyraz[-dlugosc -1]:
            return False
    return True

wyraz = 'ALA'
print(foo(wyraz))