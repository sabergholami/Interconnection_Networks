import networkx as nx
def cube_connected_cycle(n):
        g = nx.Graph()
        for x in range(0, 2 ** n):
            for y in range(0, n):
                n1 = ((y) + (x * n))
                e1 = ((y + 1) % n + (x * n))
                e2 = ((y - 1) % n + (x * n))
                e3 = ((y) + ((x ^ 2 ** y) * n))
                g.add_edge(n1, e1)
                g.add_edge(n1, e2)
                g.add_edge(n1, e3)
        return g
