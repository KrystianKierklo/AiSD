from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value = None, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


    def __repr__(self):
        return str(self.value)


    def is_leaf(self):
        if self.left_child == None and self.left_child == None:
            return True
        return False


    def add_left_child(self, value):
        self.left_child = BinaryNode(value)


    def add_right_child(self, value):
        self.right_child = BinaryNode(value)


    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)



    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)



    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)



class BinaryTree:
    root: BinaryNode


    def __init__(self, value):
        self.root=BinaryNode(value)


    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)



    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)



    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)



n1 = BinaryNode(1)
n1.add_left_child(2)
n1.left_child.add_right_child(5)
n1.left_child.add_left_child(4)
n1.left_child.left_child.add_left_child(8)
n1.left_child.left_child.add_right_child(9)
n1.add_right_child(3)
n1.right_child.add_right_child(7)




#Moja metoda polega na znalezieniu 2 sciezek od korzenia do wybranego wezla
# i zapisaniu ich do tablic z danymi, a nastepnie porownaniu tablic i odczytaniu
# rozwiazania, czyli wspolnego najblizszego wezla

#Do wyznaczenia sciezki od korzenia do wybranego wezla wykorzytuje funkcje rekurencyjna
# ktora przemierza cale drzewo w poszukiwaniu wybranego wezla, dodaje do tablicy napotkane po drodze dane,
# jesli wartosc nie bedzie na drodze do wezla to potem ja usuwa

def istnienie_sciezki(n1, tab, x):
    if (n1 == None):
        return False
    tab.append(n1.value)
    if (n1.value == x):
        return True
    if (istnienie_sciezki(n1.left_child, tab, x) or istnienie_sciezki(n1.right_child, tab, x)):
        return True
    tab.pop(-1)
    return False


# Funkcja sprawdzajaca czy podany wezel znajduje sie w drzewie, jesli tak to zwraca do niego sciezke
# w postaci tablicy danych na kolejnych wezlach od korzenia

def wyznaczenie_sciezki(n1, tab, x):
    if(istnienie_sciezki(n1, tab, x)):
        return tab

# Funkcja closest_parent korzysta z poprzednich funkcji, za ich pomoca wyznacza 2 sciezki do podanych wezlow,
# i za pomoca petli szuka pierwszej wspolnej wartosci w wczesniej odwroconych tablicach ze sciezkami do
# wybranego wezla

def closest_parent(drzewo, pierwszy_wezel, drugi_wezel):
    lista1 = []
    lista2 =[]
    wyznaczenie_sciezki(drzewo, lista1, pierwszy_wezel)
    wyznaczenie_sciezki(drzewo, lista2, drugi_wezel)
    lista1.reverse()
    lista2.reverse()
    parent = None
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                parent = lista2[j]
                return parent
                break



# Sprawdzenie czy wszystko dziala

print(closest_parent(n1, 1, 4))
print(closest_parent(n1, 8, 5))
print(closest_parent(n1, 9, 7))