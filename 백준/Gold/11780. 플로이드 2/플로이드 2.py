import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
dist = [[[] for _ in range(n+1)] for _ in range(n+1)]
path = [[-1]*(n+1) for _ in range(n+1)]  # 직전 경로 저장

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = min(graph[u][v], w)
    path[u][v] = u  # u에서 v로 가니까 path[u][v]]애는 u가 직전 경로

for i in range(n+1):
    graph[i][i] = 0

for k in range(1, n+1):

    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                dist[i][j].append(k)
                path[i][j] = path[k][j]  # k를 거치니까 path[k][j]가 직전 경로이므로 이를 대입
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if path[i][j] == -1:
            print(0)
            continue

        v = j
        ans = []
        while True:
            if v == i:
                break
            ans.append(v)
            v = path[i][v]
        print(len(ans)+1, i, *ans[::-1])
