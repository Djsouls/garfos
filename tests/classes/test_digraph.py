import collections

from garfos.classes.DiGraph import DiGraph

def test_vertex_insertion():
    dg = DiGraph()

    vertices = [i for i in range(10)]

    for v in vertices:
       dg.add_vertex(v)

    assert collections.Counter(vertices) == collections.Counter(dg.vertices.keys())
