def prims(graph):
    """
    :param graph: adj dict w weights
    :return: MST set of edges
    """
    s = list(graph.keys())[0]
    T_v = set()
    T_v.add(s)
    T_e = set()

    weights = {(u,v[0]): v[1] for u in graph for v in graph[u]}

    while len(T_v) != len(graph):
        min_weight = float('inf')
        light_edge = None
        for u,v in weights:
            if u in T_v and v not in T_v:
                if min_weight > weights[(u,v)]:
                    min_weight = weights[(u,v)]
                    light_edge = u,v
        T_v.add(light_edge[1])
        T_e.add(light_edge)
    return T_e

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

print(prims(legit))





