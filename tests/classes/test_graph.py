from garfos.classes import Graph

import collections

def test_vertex_insertion():
    g = Graph.Graph()

    vertices = [1, 2, 3, 4, 5, 6]

    for v in vertices:
        g.add_vertex(v)

    assert collections.Counter(vertices) == collections.Counter(g.vertices.keys())
