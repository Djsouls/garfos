from typing import List, Hashable

class Vertex:
    pass

class Vertex:
    def __init__(self, label: Hashable):
        self.label: Hashable = label
        self.neighbors: dict[Vertex, int] = dict()

    def add_neighbor(self, v: Vertex, weight: int = 1):
        self.neighbors[v] = weight

    def get_neighbors(self) -> List[Vertex]:
        return self.neighbors.keys()

    def degree(self) -> int:
        return len(self.neighbors)

