import networkx as nx

with open('com-youtube.ungraph.txt', 'r') as f:
	edges = [i.strip().replace('n', '').split() for i in f]

G = nx.Graph() # Initialize a Graph object                                                        
G.add_edges_from(edges) # Add edges to the Graph  
print(nx.info(G)) # Print information about the Graph  
# If your Graph has more than one component, this will return False:
print(nx.is_connected(G))

# Next, use nx.connected_components to get the list of components,
# then use the max() command to find the largest one:
components = nx.connected_components(G)
largest_component = max(components, key=len)

# Create a "subgraph" of just the largest component
# Then calculate the diameter of the subgraph, just like you did with density.
#

subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print("Network diameter of largest component:", diameter)