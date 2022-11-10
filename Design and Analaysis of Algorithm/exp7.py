# Floyd Warshall Algorithm in python

def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)


def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(len(dist)):
        for j in range(len(dist)):
            if (dist[i][j] == 999):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print("")


if __name__ == "__main__":
    graph = [[0, 3, 8, 999, -4],
             [999, 0, 999, 1, 7],
             [999, 4, 0, -5, 999],
             [2, 999, 999, 0, 999],
             [999, 999, 999, 6, 0]]
    floydWarshall(graph)
