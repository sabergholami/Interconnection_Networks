import networkx as nx
def grid(n, m):
    n = n - 1
    m = m - 1
    G = nx.empty_graph()
    for i in range(m + 1):
        for j in range(n):
            G.add_edge(((n + 1) * i) + j, ((n + 1) * i) + j + 1)
    for i in range(n + 1):
        for j in range(m):
            G.add_edge(((n + 1) * j) + i, ((n + 1) * (j + 1)) + i)
    return G
