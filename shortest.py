# Calculate the shortest path between two nodes (e.g., "A" and "C")
start_node = "A"
end_node = "C"  
shortest_path = nx.shortest_path(G, start_node, end_node)

# Calculate the length of the shortest path (number of edges)
shortest_path_length = len(shortest_path) - 1

# Print the results
print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")

print(f"Shortest path length: {shortest_path_length} edge(s)")

