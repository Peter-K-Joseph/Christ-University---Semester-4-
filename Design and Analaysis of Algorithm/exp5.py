# Kruskal’s Minimum Spanning tree algorithm

parent = []

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b
    
def kruskal(cost):
    mincost = 0
    for i in cost:
        if find(i[0]) != find(i[1]):
            union(i[0], i[1])
            print('Edge {}: {} - {}'.format(i[0], i[1], i[2]))
            mincost += i[2]
    print('Minimum cost = {}'.format(mincost))
    
if __name__ == '__main__':
    nodes = int(input('Enter number of nodes: '))
    edges = int(input('Enter number of edges: '))
    cost = []
    print('Enter edges in format: ')
    for i in range(edges):
        u = int(input("Enter initial node: "))
        v = int(input("Enter final node: "))
        w = int(input("Enter cost to move from {} to {}: ".format(u, v)))
        cost.append([u, v, w])
    cost.sort(key = lambda item: item[2])
    for i in range(nodes):
        parent.append(i)
    kruskal(cost)