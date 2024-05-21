# --- 요구 사항 ---
# 준형이와 친구들은 서로 다른 도시에 살고 있다.
# 도시를 연결하는 도로는 일방 통행만 있어서 도시 Ai에서 Bi로 가는 시간과 Bi에서 Ai로 가는 시간이 다를 수 있다.
# - 왕복시간은 자신이 살고 있는 도시에서 도시 X로 이동하는 시간과 도시 X에서 다시 자신이 살고 있는 도시로 이동하는 시간의 합
# - 준형이와 친구들이 갈 수 있는 도시만 선택
# - 준형이와 친구들의 왕복시간 들 중 최대가 최소가 되는 도시 X를 선택
# - 준형이와 친구들이 이동할 수 있는 도시가 최소한 하나 이상이 있음을 보장

# TODO: 아래 조건을 만족하는 도시 X를 선택하여 거기서 만나려고 한다.

# --- 풀이 방법 ---
# Ai에서 Bi로 이동하는 시간 주어짐
# 총 인원, 살고 있는 도시 주어짐


# 준형이와 친구들이 왕복시간이 가장 적게 걸리는 도시 X 선택
# 모든 지점에서 모든 지점까지의 최단 거리 테이블을 구하고 왕복시간 합의 최소가 되는 도시 X 결정

import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
for i in range(1, n+1):
    graph[i][i] = 0

total = int(input())
livedCities = list(map(int, input().split()))

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

dist = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    maxValue = 0
    for c in livedCities:
        if c == i or graph[c][i] == INF or graph[i][c] == INF:
            continue
        maxValue = max(maxValue, graph[c][i] + graph[i][c])
    dist[i] = maxValue

answer = []
minDist = min(dist[1:])
for x in range(1, n+1):
    if dist[x] == minDist:
        answer.append(x)
print(*answer)
