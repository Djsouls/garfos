from typing import Union, Hashable

class Vertex:
    pass

class Vertex:
    def __init__(self, label: Hashable):
        self.label: Hashable = label
        self.neighbors: dict[Vertex, int] = dict()

    def add_neighbor(self, v: Vertex, weight: int = 1):
        self.neighbors[v] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def degree(self):
        return len(self.neighbors)

class Graph:
    def __init__(self):
        self.vertices: dict[Hashable, Vertex] = dict()

    def add_edge(self, v1: Hashable, v2: Hashable, weight: int = 1):
        v1 = self.add_vertex(v1)
        v2 = self.add_vertex(v2)

        self.connect(v1, v2, weight)

    def add_vertex(self, v: Hashable):
        if v in self.vertices:
            return self.vertices[v]

        v1 = Vertex(v)

        self.vertices[v] = v1

        return v1

    def connect(self, v1: Vertex, v2: Vertex, weight: int = 1):
        v1.add_neighbor(v2, weight)
        v2.add_neighbor(v1, weight)

    def neighbors(self, v: Hashable):
        return self.vertices[v].get_neighbors()
