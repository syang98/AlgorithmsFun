from union_find import UnionFind

def kruskals(graph):
    """
    :param graph: undigraph
    :return:
    """
    T = set() # empty edge set
    union_find = UnionFind()
    new = {}
    for v in graph:
        new_edges = []
        set_v = union_find.make_set(v)
        for u, w in graph[v]:
            new_edges.append((union_find.make_set(u), w))
        new[set_v] = new_edges

    edges = [(u,v[0],v[1]) for u in new for v in new[u]]
    edges.sort(key=lambda x: x[-1])

    for u,v,_ in edges:
        if union_find.find_set(u) != union_find.find_set(v):
            T.add((union_find.get_key(u),union_find.get_key(v)))
            union_find.union(u, v)
    return T

example = {
    "A": [("B", 1), ("D", 3), ("C", 4)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 5)],
    "D": [("A", 3), ("C", 5), ("B", 2)]
}


legit = {
    "A": [("B", 8), ("C", 2), ("F", 3), ("D", 4)],
    "B": [("A", 8), ("E", 9)],
    "C": [("A", 2), ("E", 6), ("F", 1)],
    "D": [("A", 4), ("E", 7), ("F", 5)],
    "E": [("C", 6), ("B", 9), ("D", 7)],
    "F": [("C", 1), ("G", 10)],
    "G": [("F", 10)]
}
print(kruskals(legit))