# Prim's minimum spanning tree code and find the minimun weight of the spanning tree
INF = 9999999
G = [[INF, 4, 4 , INF, INF, INF],
     [4, INF, 2, INF, INF, INF],
     [4, 2, INF, 3, 2, 4],
     [INF, INF, 3, INF, INF, 3],
     [INF, INF, 2, INF, INF, 3],
     [INF, INF, 4, 3, 3, INF]]
selected = []
V = len(G[0])
for i in range(V):
    selected.append(0)
no_edge = 0
cost = 0
selected[0] = True
print("Edge\tWeight\n")
while (no_edge < V - 1):
    minimum = INF
    init_node = 0
    dest_node = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        init_node = i
                        dest_node = j
    print("{} to {} \t {}".format(init_node, dest_node, G[init_node][dest_node]))
    cost += G[init_node][dest_node]
    selected[dest_node] = True
    no_edge += 1
print("Max Cost: {}". format(cost))