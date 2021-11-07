from garfos.classes.Graph import Graph
from garfos.classes.Vertex import Vertex


class DiGraph(Graph):
    def __init__(self):
        super().__init__()

    def connect(self, v1: Vertex, v2: Vertex, weight: int = 1):
        v1.add_neighbor(v2, weight)

