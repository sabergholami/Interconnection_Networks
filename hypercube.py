import networkx as nx
def hypercube_graph(n):
    H = nx.Graph()
    for i in range(2 ** n):
        for j in range(n):
            H.add_edge(i, i ^ 2 ** j)
    return H
