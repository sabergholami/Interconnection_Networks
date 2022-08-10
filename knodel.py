import networkx as nx
def knodel(delta, n):
    G = nx.empty_graph()
    if n % 2 != 0:
        print('n must be even!')
        return G
    else:
        m = int(n / 2)
        ne_li = []
        for k in range(delta):
            ne_li.append(2 ** k - 1)
        for i in range(1, m + 1):
            for k in ne_li:
                if i + m + k > n:
                    G.add_edge(i, i + k)
                else:
                    G.add_edge(i, (i + m + k))
        print(G.edges())
        return G
