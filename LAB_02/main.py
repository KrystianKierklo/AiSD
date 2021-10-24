class Node():
    def __init__(self, dane):
        self.dane = dane
        self.nastepny = None

    def __repr__(self):
        return str(self.dane)

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None


    def __repr__(self):
        licznik = self.head
        tab = []
        while licznik != None:
            tab.append(str(licznik.dane))
            licznik = licznik.nastepny
        return " -> ".join(tab)


    def push(self, dane):
        begin_node = Node(dane)
        begin_node.nastepny = self.head
        self.head = begin_node


    def append(self, dane):
        added_node = Node(dane)
        if self.head == None:
            self.head = added_node
        licznik = self.head
        while licznik.nastepny != None:
            licznik = licznik.nastepny
        licznik.nastepny = added_node


    def node(self, pozycja):
        licznik = self.head
        while(pozycja>0):
            if(licznik.nastepny != None):
                licznik = licznik.nastepny
                pozycja -= 1
            else:
                print("\nNie ma takiego indeksu :(")
                return None
        return licznik


    def insert(self, dane, po_jakich):
        insert_node = Node(dane)
        insert_node.nastepny = po_jakich.nastepny
        po_jakich.nastepny = insert_node


    def pop(self):
        licznik = self.head
        self.head = licznik.nastepny
        return licznik.dane


    def remove_last(self, ostatni):
        licznik = self.head
        while (licznik.nastepny.nastepny != ostatni):
            licznik = licznik.nastepny
        removed_node = licznik.nastepny.nastepny
        licznik.nastepny.nastepny = None
        return removed_node


    def remove(self, indeks):
        licznik = self.head
        while (licznik.nastepny != indeks.nastepny):
            licznik = licznik.nastepny
        licznik.nastepny = indeks.nastepny.nastepny



    def wyswietl(self):
        licznik = self.head
        print(licznik.dane)
        while licznik.nastepny != None:
            print(licznik.nastepny.dane)
            licznik = licznik.nastepny


def len(lista):
    licznik = lista.head
    wynik = 0
    while licznik.nastepny != None:
        licznik = licznik.nastepny
        wynik += 1
    return wynik + 1


def foo_print(lista):
    print(repr(lista))



lista = LinkedList()

assert lista.head == None

lista.push(1)
lista.push(0)
#foo_print(lista)
assert str(lista) == '0 -> 1'

lista.append(9)
lista.append(10)
assert str(lista) == '0 -> 1 -> 9 -> 10'

middle_node = lista.node(pozycja=1)
lista.insert(5, po_jakich=middle_node)
assert str(lista) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = lista.node(pozycja=0)
returned_first_element = lista.pop()
assert first_element.dane == returned_first_element

last_element = lista.node(pozycja=3)
returned_last_element = lista.remove_last(last_element)
assert last_element == returned_last_element # usunalem .dane
assert str(lista) == '1 -> 5 -> 9'

second_node = lista.node(pozycja=1)
lista.remove(second_node)
assert str(lista) == '1 -> 5'

#print("\nDlugosc listy wynosi: " ,len(lista))
