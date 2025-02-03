import random
import networkx as nx
import matplotlib.pyplot as plt

# Number of nodes
num_nodes = 40
max_cost = 10

def generate_graph(num_nodes, max_cost):
    graph = {i: {} for i in range(num_nodes)}
    
    for i in range(num_nodes):
        num_edges = random.randint(1, min(5, num_nodes - 1))  # Ensure connectivity
        neighbors = random.sample(range(num_nodes), num_edges)
        for neighbor in neighbors:
            if neighbor != i:
                cost = random.randint(1, max_cost)
                graph[i][neighbor] = cost
                graph[neighbor][i] = cost  # Ensure undirected graph
    
    return graph

def draw_graph(graph):
    G = nx.Graph()
    
    for node, edges in graph.items():
        for neighbor, cost in edges.items():
            G.add_edge(node, neighbor, weight=cost)
    
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Generate and draw the graph
graph = generate_graph(num_nodes, max_cost)
draw_graph(graph)
