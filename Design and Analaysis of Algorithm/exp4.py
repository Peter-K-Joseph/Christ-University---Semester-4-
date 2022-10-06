# Dijkstra’s Shortest Path Algorithm 

def dijkstra(graph, start, end):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph
    infinity = 9999999
    path = []
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node
        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)
    current_node = end
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[end] != infinity:
        print(shortest_distance[end])
        print(path)
    else:
        print('Path not reachable')
        
graph = {
    'A': {'B': 1, 'F': 8, 'G': 9},
    'B': {'A': 1, 'D': 1, 'F': 3},
    'D': {'B': 1, 'E': 9, 'I': 2},
    'E': {'F': 4, 'G': 9, 'D': 9, 'H': 1},
    'F': {'A': 8, 'B': 3, 'G': 3, 'E': 4},
    'G': {'A': 9, 'E': 9, 'F': 3, 'H': 10},
    'H': {'G': 10, 'E': 1, 'I': 9, 'K': 4, 'L': 3},
    'I': {'D': 2, 'H': 9, 'K': 2, 'L': 1},
    'K': {'H': 4, 'I': 2, 'L': 4},
    'L': {'H': 3, 'I': 1, 'K': 4}
}

dijkstra(graph, 'A', 'L')