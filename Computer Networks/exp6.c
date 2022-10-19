// implement dijkstra's algorithm

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#define MAX 100

int n; // number of vertices in the graph
int adj[MAX][MAX]; // adjacency matrix
int weight[MAX][MAX]; // weight matrix
int pred[MAX]; // array to store predecessor of a vertex
int dist[MAX]; // array to store distance of a vertex from source

// function prototypes
void dijkstra(int s);
void printPath(int s, int v);

int main() {
	int i, j, s, v;
	
	printf("Enter number of vertices in graph: ");
	scanf("%d", &n);
	
	for (i = 0; i < n; i++) {
		printf("\n\nAdjacemt Matrix data for %d\n", i);
		for (j = 0; j < n; j++) {
			adj[i][j] = INT_MAX;
			if (i == j) {
				weight[i][j] = 0;
				continue;
			}
			printf("Enter cost of travel from %d to %d (press -1 if no path): ", i, j);
			scanf("%d", &weight[i][j]);
			if (weight[i][j] == -1)
				weight[i][j] = INT_MAX;
		}		 
	}

	printf("Enter the source vertex: ");
	scanf("%d", &s);

	printf("Enter the destination vertex: ");
	scanf("%d", &v);

	dijkstra(s);
	printf("nShortest path from vertex %d to vertex %d is: ", s, v);
	printPath(s, v);
	return 0;
}

void dijkstra(int s) {
	int i, j, u, count, mindist;
	int visited[MAX];

	// initialize pred[], dist[] and visited[]
	for (i = 0; i < n; i++) {
		pred[i] = s;
		dist[i] = weight[s][i];
		visited[i] = 0;
	}

	dist[s] = 0;
	visited[s] = 1;
	count = 1;

	while (count < n - 1) {
		mindist = INT_MAX;

	// next node is minimum distance node in unvisited nodes
	for (i = 0; i < n; i++)
		if (dist[i] < mindist && !visited[i]) {
			mindist = dist[i];
			u = i;
		}

	visited[u] = 1;
	count++;

	for (i = 0; i < n; i++)
		if (!visited[i] && adj[u][i] && mindist + weight[u][i] < dist[i]) {
			dist[i] = mindist + weight[u][i];
			pred[i] = u;
		}
	}
}

void printPath(int s, int v) {
	if (v == s) {
		printf("%d ", v);
		return;
	}
	printPath(s, pred[v]);
	printf("%d ", v);
}
