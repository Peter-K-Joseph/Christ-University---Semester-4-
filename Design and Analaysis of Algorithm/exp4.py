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
    'A': {'B': 7, 'C': 9, 'D': 7},
    'B': {'A': 7, 'C': 6, 'D': 5},
    'C': {'A': 9, 'B': 6, 'D': 8, 'E': 1},
    'D': {'A': 7, 'B': 5, 'C': 8, 'E': 6, 'F': 4},
    'E': {'A': 1, 'C': 7, 'D': 6, 'F': 2},
    'F': {'D': 4, 'E': 2}
}

dijkstra(graph, 'C', 'A')