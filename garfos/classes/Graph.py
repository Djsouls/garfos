from typing import List, Hashable

from garfos.classes.Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices: dict[Hashable, Vertex] = dict()

    def add_edge(self, v1: Hashable, v2: Hashable, weight: int = 1):
        v1 = self.add_vertex(v1)
        v2 = self.add_vertex(v2)

        self.connect(v1, v2, weight)

    def add_vertex(self, v: Hashable) -> Vertex:
        if v in self.vertices:
            return self.vertices[v]

        v1 = Vertex(v)
        self.vertices[v] = v1

        return v1

    def connect(self, v1: Vertex, v2: Vertex, weight: int = 1):
        v1.add_neighbor(v2, weight)
        v2.add_neighbor(v1, weight)

    def neighbors(self, v: Hashable) -> List[Vertex]:
        return self.vertices[v].get_neighbors()
