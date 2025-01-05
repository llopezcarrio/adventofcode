import networkx as nx
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

G = nx.Graph()
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        u, v = line.strip().split("-")
        G.add_edge(u, v)

max_clique = max(nx.find_cliques(G), key=len)
max_clique = ",".join(sorted(max_clique))
print(max_clique)