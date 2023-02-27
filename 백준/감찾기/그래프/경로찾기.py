import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

INF = int(1e9)
distance = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            distance[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = 1

for i in range(n):
    for j in range(n):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
