from union_find import UnionFind


def cycles(graph):
    union_find = UnionFind()
    new = {}
    for v in graph:
        new_edges = []
        set_v = union_find.make_set(v)
        for u in graph[v]:
            new_edges.append(union_find.make_set(u))
        new[set_v] = new_edges

    for u_ in new:
        for v_ in new[u_]:
            if union_find.find_set(u_) == union_find.find_set(v_):
                return True
            else:
                union_find.union(u_, v_)
    return False


example = {"a":["b", "c"], "b":["a"], "c":["a", "b"]}

print(cycles(example))