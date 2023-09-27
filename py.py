import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
triangle_edges = [("A", "B"), ("B", "C"), ("C", "A")]
star_edges = [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E")]
G = nx.from_edgelist(star_edges)

import networkx as nx
import matplotlib.pyplot as plt

# Define the edges of the graph
star_edges = [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E")]

num_nodes = 4

# Create a graph
G = nx.Graph()
G.add_edges_from(star_edges)

# Get the size of the graph (number of edges)
graph_size = G.size()

# Get the order of the graph (number of nodes)
graph_order = G.order()

# Get the maximum degree of the graph
max_degree = max(dict(G.degree()).values())

# Print the results
print("Tamaño del grafo:", graph_size)
print("Orden del grafo:", graph_order)
print("Grado máximo del grafo:", max_degree)


# Draw the graphn
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=1000)
plt.show()

