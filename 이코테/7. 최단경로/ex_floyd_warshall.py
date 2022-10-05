INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 : 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# a에서 b로 가는 비용 : c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # a에서 b로 갈 때, k를 거쳐서 가는게 빠르면 갱신
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INF")
        else:
            print(graph[i][j], end=' ')
    print()