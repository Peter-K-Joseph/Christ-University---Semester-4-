# Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

def hamiltonianCycle(G, n):
    path = []
    path.append(0)
    if not hamCycleUtil(G, path, n):
        print("Solution does not exist")
        return False
    printSolution(path)
    return True

def hamCycleUtil(G, path, n):
    if len(path) == n:
        if G[path[-1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, n):
        if isSafe(G, v, path):
            path.append(v)
            if hamCycleUtil(G, path, n):
                return True
            path.pop()
    return False

def isSafe(G, v, path):
    if G[path[-1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def printSolution(path):
    print("Solution Exists: Following is one Hamiltonian Cycle")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0], end=" ")
    
if __name__ == "__main__":
    G = [[0, 1, 0, 1, 0],
         [1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 1, 1, 0]]
    hamiltonianCycle(G, 5)