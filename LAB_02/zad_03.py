from main import *
from zad_02 import *

class Queue:
    def __init__(self):
        self.head = None


    def __repr__(self):
        licznik = self.head
        tab = []
        while licznik != None:
            tab.append(str(licznik.dane))
            licznik = licznik.nastepny
        return ", ".join(tab)


    def peek(self):
        return self.head


    def enqueue(self, element):
        enqueue_node = Node(element)
        if self.head == None:
            self.head = enqueue_node
        else:
            licznik = self.head
            while licznik.nastepny != None:
                licznik = licznik.nastepny
            licznik.nastepny = enqueue_node


    def dequeue(self):
        dequeue_node = self.head
        self.head = dequeue_node.nastepny
        return str(dequeue_node)


def len(queue):
    dlugosc = 0
    licznik = queue.head
    while licznik != None:
        licznik = licznik.nastepny
        dlugosc += 1
    return dlugosc



queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
