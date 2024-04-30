def generate_adjacency_matrix(num_nodes, edge_list):
     #for _ in range(num_nodes):
         #adjacency_matrix = adjacency_matrix+(0 * num_nodes)
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]


    for edge in edge_list:
        node1, node2 = edge
        adjacency_matrix[node1][node2] = 1
        adjacency_matrix[node2][node1] = 1

    return adjacency_matrix


# Example usage
num_nodes = 5
edges = [(0, 1), (0, 2),(0,4), (1, 4), (2, 3), (3, 4)]
adj_matrix = generate_adjacency_matrix(num_nodes, edges)
for row in adj_matrix:
    print(row)
