# --- 요구 사항 ---
# 각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결
# 양방향 통행이 가능
# 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능
# 얻을 수 있는 아이템의 최대 개수
# 모든 지점에서 모든 지점까지의 최단거리(최단거리로 가야 최대 아이템 개수)

# --- 풀이 방법 ---
# 거리를 누적값으로 저장하는 배열 필요
# 거쳐서 갈 수 있으면 수색 범위와 해당 거리를 비교하여 카운팅
# 100 * 100 * 100 = 10^6

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
dist = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(r):
    a, b, i = map(int, input().split())
    graph[a][b] = i
    graph[b][a] = i

for i in range(n):
    dist[i+1][i+1] = items[i]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] <= m:
            dist[i][j] += items[j-1]
answer = 0
for i in dist:
    answer = max(answer, sum(i))
print(answer)
