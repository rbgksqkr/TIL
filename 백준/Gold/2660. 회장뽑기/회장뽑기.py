# 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구 또는 친구의 친구
# 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이 -> 최단거리
# 회장은 회원들 중에서 점수가 가장 작은 사람
# 회장의 점수와 회장이 될 수 있는 모든 사람을 찾기
# --- 풀이 방법 ---
# 서로 친구 -> 양방향 그래프
# 그래프 연결 상태를 저장할 2차원 배열 저장. graph[a].append(b); graph[b].append(a);
# graph = [[], [2], [1, 3, 4], [2, 4, 5], [2, 3, 5], [3, 4]]
# 모든 점에서 모든 점까지의 최단거리 -> 플로이드 50 * 50 * 50 = 10만

import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]

while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    graph[u].append(v)
    graph[v].append(u)
    dist[u][v] = 1
    dist[v][u] = 1

for i in range(1, n+1):
    dist[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                
max_count = 0
max_arr = []
for i in dist:
    max_arr.append(max(i[1:]))
answer = min(max_arr)
result = []
for idx, i in enumerate(max_arr):
    if i == answer:
        result.append(idx)

print(answer, len(result))
result.sort()
for i in result:
    print(i, end=' ')
