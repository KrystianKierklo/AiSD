from main import *

class Stack():
    def __init__(self):
        self.head = None


    def __repr__(self):
        licznik = self.head
        tab = []
        while licznik != None:
            tab.append(str(licznik.dane))
            licznik = licznik.nastepny
        return "\n".join(tab)


    def push(self, element):
        if self.head == None:
            self.head = Node(element)
        else:
            push_node = Node(element)
            push_node.nastepny = self.head
            self.head = push_node


    def pop(self):
        if self.head == None:
            return None
        else:
            pop_value = self.head.dane
            self.head = self.head.nastepny
            return pop_value


def foo_print(stack):
    print(repr(stack))


def foo_len(stack):
    dlugosc = 0
    licznik = stack.head
    while licznik != None:
        licznik = licznik.nastepny
        dlugosc += 1
    return dlugosc



stack = Stack()

assert foo_len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3

top_value = stack.pop()
assert top_value == 1

assert len(stack) == 2
