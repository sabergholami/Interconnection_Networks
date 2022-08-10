import networkx as nx
def torus(n, m):
    G = nx.empty_graph()
    for i in range(m + 1):
        for j in range(n):
            G.add_edge(((n + 1) * i) + j, ((n + 1) * i) + j + 1)
        G.add_edge((n + 1) * i, (n + 1) * (i + 1) - 1)
    for i in range(n + 1):
        for j in range(m):
            G.add_edge(((n + 1) * j) + i, ((n + 1) * (j + 1)) + i)
        G.add_edge(i, i + (m * (n + 1)))
    return G
