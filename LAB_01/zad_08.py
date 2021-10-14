lista = []
n = int(input("Wprowadz ile liczb bedziesz chcial wprowadzic: "))

for i in range (0,n):
    k = input("Wprowadz liczbe: ")
    lista.append(k)

krotka = tuple(lista)
print(krotka)