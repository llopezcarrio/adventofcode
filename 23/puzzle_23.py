import networkx as nx
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

G = nx.Graph()
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        u, v = line.strip().split("-")
        G.add_edge(u, v)

triangles = []
for clique in nx.enumerate_all_cliques(G):
    if len(clique) == 3:
        triangles.append(clique)
    if len(clique) > 3:
        break

# Filter for cliques containing at least one node starting with 't'
triangles_with_t = sum(
    1 for triangle in triangles if any(node.startswith("t") for node in triangle)
)

# Print results
print(triangles_with_t)