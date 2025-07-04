import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1


for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()