from typing import Any
from typing import Optional
from typing import Dict, List


class Vertex:
    data: Any
    index: int

    def __init__(self, data, index):
        self.data = data
        self.index = index

    def __repr__(self):
        return f'{self.data}'


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f'{self.source}{self.destination} = {self.weight}'




class Graph:
    adjacencies: Dict[Vertex, List[Edge]]


    def __init__(self):
        self.adjacencies = dict()

    def __repr__(self):
        return str(self.adjacencies)


    def create_vertex(self, data: Any):
        self.adjacencies[Vertex(data, len(self.adjacencies))] = list()


    def add(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))



class GraphPath:
    graf: Graph
    start: Vertex
    end: Vertex

    def __init__(self, graf: Graph, start: Vertex, end: Vertex):
        self.graf = graf
        self.start = start
        self.end = end

    def algorytm_dijksry(self):
        tablica_kosztow: Dict[Vertex, int] = {self.end: float('inf')}
        tablica_rodzicow: Dict[Vertex, int] = {self.end: None}
        odwiedzony = []

        for wierzcholek in self.graf.adjacencies[self.start]:
            tablica_kosztow[wierzcholek.destination] = wierzcholek.weight
            tablica_rodzicow[wierzcholek.destination] = self.start

        v = min(tablica_kosztow, key=tablica_kosztow.get)
        while v:
            c = tablica_kosztow.get(v)
            odwiedzony.append(v)
            for sasiad in self.graf.adjacencies[v]:
                if sasiad.destination in odwiedzony:
                    continue
                nc = c + sasiad.weight
                if not sasiad.destination in tablica_rodzicow:
                    tablica_rodzicow[sasiad.destination] = v
                    tablica_kosztow[sasiad.destination] = tablica_kosztow[v] + sasiad.weight
                else:
                    if nc < tablica_kosztow[sasiad.destination]:
                        tablica_kosztow[sasiad.destination] = nc
                        tablica_rodzicow[sasiad.destination] = v

            bez_odwiedzonych = dict()
            for wierzcholek, waga in tablica_kosztow.items():
                if wierzcholek not in odwiedzony:
                    bez_odwiedzonych[wierzcholek] = waga
            if not bez_odwiedzonych:
                break
            v = min(bez_odwiedzonych, key=bez_odwiedzonych.get)

        node = self.end
        droga = [str(node.data)]
        while node is not self.start:
            node = tablica_rodzicow[node]
            droga.insert(0, str(node.data))
        return droga



def all_weighted_shortest_paths(graf, start) -> dict:
    trasa: Dict[Any, List[Edge]] = dict()
    for key in graf.adjacencies.keys():
        if key is start:
            continue
        path = GraphPath(graf, start, key)
        trasa[key] = path.algorytm_dijksry()
    return trasa



graf = Graph()

wierzcholki = ["A", "B", "C", "D"]
for x in wierzcholki:
    graf.create_vertex(x)

lista_kluczy = [x for x in graf.adjacencies.keys()]

graf.add(lista_kluczy[0], lista_kluczy[1], 30)
graf.add(lista_kluczy[0], lista_kluczy[2], 10)
graf.add(lista_kluczy[1], lista_kluczy[3], 2)
graf.add(lista_kluczy[2], lista_kluczy[3], 9)
graf.add(lista_kluczy[1], lista_kluczy[2], 5)

print("GRAF PIERWSZY: ", all_weighted_shortest_paths(graf, lista_kluczy[0]))



graf2 = Graph()

wierzcholki2 = ["A", "B", "C", "D", "E"]
for x in wierzcholki2:
    graf2.create_vertex(x)

lista_kluczy2 = [x for x in graf2.adjacencies.keys()]

graf2.add(lista_kluczy2[0], lista_kluczy2[1], 8)
graf2.add(lista_kluczy2[0], lista_kluczy2[4], 15)
graf2.add(lista_kluczy2[1], lista_kluczy2[2], 12)
graf2.add(lista_kluczy2[1], lista_kluczy2[4], 3)
graf2.add(lista_kluczy2[2], lista_kluczy2[4], 2)
graf2.add(lista_kluczy2[2], lista_kluczy2[3], 5)
graf2.add(lista_kluczy2[3], lista_kluczy2[4], 14)

print("GRAF DRUGI: ", all_weighted_shortest_paths(graf2, lista_kluczy2[0]))



graf3 = Graph()

wierzcholki3 = ["A", "B", "C", "D", "E", "F"]
for x in wierzcholki3:
    graf3.create_vertex(x)

lista_kluczy3 = [x for x in graf3.adjacencies.keys()]

graf3.add(lista_kluczy3[0], lista_kluczy3[1], 7)
graf3.add(lista_kluczy3[0], lista_kluczy3[5], 10)
graf3.add(lista_kluczy3[1], lista_kluczy3[2], 11)
graf3.add(lista_kluczy3[1], lista_kluczy3[5], 9)
graf3.add(lista_kluczy3[2], lista_kluczy3[3], 4)
graf3.add(lista_kluczy3[3], lista_kluczy3[4], 1)
graf3.add(lista_kluczy3[3], lista_kluczy3[5], 4)
graf3.add(lista_kluczy3[4], lista_kluczy3[5], 6)

print("GRAF TRZECI: ", all_weighted_shortest_paths(graf3, lista_kluczy3[0]))



print("\n", graf, "\n", graf2, "\n", graf3)