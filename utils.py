import networkx as nx

def parse_input(nodes, edges):
    node_list = [node.strip() for node in nodes.split(",")]
    graph = {node: [] for node in node_list}

    G = nx.Graph()

    for line in edges.split("\n"):
        if line.strip() == "":
            continue

        u, v, w = line.split(",")
        u, v = u.strip(), v.strip()
        w = int(w.strip())

        graph[u].append((v, w))
        graph[v].append((u, w))

        G.add_edge(u, v, weight=w)

    return graph, G