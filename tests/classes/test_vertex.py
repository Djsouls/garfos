from garfos.classes import Graph

import collections

DEFAULT_WEIGHT = 1

def test_add_neighbors():
    v = Graph.Vertex(-1)

    neighbors = [Graph.Vertex(i) for i in range(10)]

    for n in neighbors:
        v.add_neighbor(n)

    assert collections.Counter(neighbors) == collections.Counter(v.get_neighbors())

def test_add_neighbors_default_weight():
    v = Graph.Vertex(-1)

    neighbors = [Graph.Vertex(i) for i in range(10)]

    for n in neighbors:
        v.add_neighbor(n)

    for n in neighbors:
        assert v.neighbors[n] == DEFAULT_WEIGHT

def test_add_neighbors_different_weight():
    v = Graph.Vertex(-1)

    vertex_weight = {Graph.Vertex(n): n * 2 for n in range(10)}

    for n, w in vertex_weight.items():
        v.add_neighbor(n, w)

    for n in v.get_neighbors():
        assert vertex_weight[n] == v.neighbors[n]

def test_degree():
    degree = 10

    v = Graph.Vertex(-1)

    neighbors = [Graph.Vertex(i) for i in range(degree)]

    for n in neighbors:
        v.add_neighbor(n)

    assert v.degree() == degree
