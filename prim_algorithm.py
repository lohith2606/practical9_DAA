import heapq

def prim_mst(graph, num_vertices):
    """
    Finds the Minimum Spanning Tree (MST) using Prim's Algorithm.
    
    :param graph: Dict representing an adjacency list: { vertex: [(neighbor, weight), ...] }
    :param num_vertices: Total number of vertices in the graph
    :return: A tuple containing (list of MST edges, total weight of the MST)
    """
    # Track vertices included in the MST
    visited = [False] * num_vertices
    
    # Priority Queue stores tuples of: (edge_weight, parent_node, current_node)
    # Start arbitrarily from vertex 0 with an initial weight of 0 and no parent (-1)
    min_heap = [(0, -1, 0)]
    
    mst_edges = []
    total_weight = 0
    edges_count = 0

    while min_heap and edges_count < num_vertices:
        weight, parent, u = heapq.heappop(min_heap)
        
        # If the vertex is already in the MST, skip it to prevent cycles
        if visited[u]:
            continue
            
        # Include vertex in MST
        visited[u] = True
        total_weight += weight
        
        # If it's not the starting vertex, record the edge
        if parent != -1:
            mst_edges.append((parent, u, weight))
            edges_count += 1
            
        # Explore and push all adjacent edges of the current vertex
        for neighbor, edge_weight in graph.get(u, []):
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, u, neighbor))
                
    return mst_edges, total_weight


# --- Execution Example ---
if __name__ == "__main__":
    # Define an undirected graph with 5 vertices (0 to 4)
    # Format: { vertex: [(neighbor, weight), ...] }
    example_graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }
    
    num_v = 5
    mst, weight = prim_mst(example_graph, num_v)
    
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"Edge {u} - {v} with weight {w}")
        
    print(f"\nTotal MST Weight: {weight}")
