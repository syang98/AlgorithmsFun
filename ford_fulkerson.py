def dfs(graph, s, t):
    """
    :param graph: adj dict, our current flow
    :param s: source
    :param t: sink
    :return: path between source and sink if there is one, else None
    """
    parent = {}
    for u, in graph:
        for v in graph[u]:
            parent[u] = None
            parent[v] = None

    parent[s] = s
    if s not in graph:
        return None

    def search(graph_, u):
        for v in graph_[u]:
            if parent[v[0]] is None:
                parent[v[0]] = u
                search(graph_, v[0])
    search(graph, s)

    def make_path(parent_, t_):
        if parent_[t_] is None:
            return None
        else:
            path = [t_]
            while parent_[t_] != t_:
                if parent_[t_] is None:
                    # might be unnecessary, but I won't test it now, maybe once test is over
                    return None
                path.append(parent_[t_])
                t_ = parent_[t_]
        return path[::-1]

    # processing this so I can use it, want it to look like:
    # [(s,u, flow), ... ]
    node_only = make_path(parent, t)
    if node_only is None:
        return None
    return [(node_only[i], node_only[i+1], graph[node_only[i]][node_only[i+1]]) for i in range(len(node_only)-1)]


def edge_set(network):
    """
    :param network: a digraph
    :return: all edges
    """
    return {(u,v[0]) for u in network for v in network[u]}


def residual(network, capacities, E):
    """
    :param network: a digraph, specifically our current flow
    :param capacities: dict of edge to capacity
    :param E: edge set, necessary, must check of original edge set each time
    :return: a residual network see comments for how it is made
    """
    G_f = {}
    for u,v in E:
        # if capacities[(u,v)] > 0:
            # network looks like {u: (v, flow)}
        residual_capacity = capacities[(u,v)] - network[u][v]
        if residual_capacity > 0:
            G_f.setdefault(u, {}).setdefault(v, residual_capacity)
        if network[u][v] > 0:
            G_f.setdefault(v, {}).setdefault(u, network[u][v])
    return G_f


def ford_fulkerson(network, s, t):
    """
    :param network: a digraph w/ capacities
    :param s: source
    :param t: sink
    :return: max flow in the network
    """
    E = edge_set(network)

    capacities = {(u,v):network[u][v] for u,v in E}

    flow = {}
    for u in network:
        for v in network[u]:
            flow.setdefault(u, {}).setdefault(v, 0)

    G_f = residual(flow, capacities, E)
    G_f[t] = {}

    while True:
        s_t_path = dfs(G_f, s, t)
        if s_t_path is None:
            return sum([flow[s][u] for u in flow[s]])
        bottle_neck_capacity = min([edge[-1] for edge in s_t_path])
        for u, v, _ in s_t_path:
            if (u,v) in E:
                flow[u][v] += bottle_neck_capacity
            else:
                flow[v][u] -= bottle_neck_capacity
        G_f = residual(flow, capacities, E)
        G_f[t] = {}


network = {"s":{"a":3,"b":2},
           "b":{"a":3,"c":3},
           "a":{"d":2},
           "d":{"b":1,"t":3},
           "c": {"d":2,"t":2},
           "t": {}
           }

print(ford_fulkerson(network, "s", "t"))




