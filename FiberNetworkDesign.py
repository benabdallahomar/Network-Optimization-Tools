import networkx as nx

# Create a graph to represent the network
network = nx.Graph()

# Add nodes and edges with distances (in km) representing the fiber-optic cables
network.add_edge('A', 'B', weight=10)
network.add_edge('B', 'C', weight=15)
network.add_edge('A', 'C', weight=20)
network.add_edge('C', 'D', weight=30)
network.add_edge('B', 'D', weight=25)

# Compute the shortest path using Dijkstra's algorithm
shortest_path = nx.dijkstra_path(network, source='A', target='D')
path_length = nx.dijkstra_path_length(network, source='A', target='D')

print(f"Shortest path from A to D: {shortest_path} with length {path_length} km")
