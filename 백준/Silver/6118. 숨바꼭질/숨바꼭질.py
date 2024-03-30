# * `인접 리스트`로 입력이 주어질 때 특정 노드에서 가장 멀리 떨어진 노드와의 거리 구하기 : `최대거리`
# --- 풀이 방법 ---
# 각 노드가 어떤 노드와 연결되어 있는지 2차원 배열에 담기
# [[], [2, 3], [3, 4, 5], [1, 2, 4, 6], [2, 3], [2], [3, 7]]
# 양끝이 중복되어 거리가 갱신될 수 있으므로 dist 배열에 저장 필요
# dist = [0, 0, 0, 0, 0, 0, 0]
# dist = [0, 0, 1, 1, 0, 0, 0]
# dist = [0, 0, 1, 1, 2, 2, 2]
# dist = [0, 0, 1, 1, 2, 2, 2]
# dist 최댓값 구하기

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
dist = [INF for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
dist[1] = 0
visited = [0 for _ in range(n+1)]
while queue:
    x = queue.popleft()

    for i in graph[x]:
        if not visited[i]:
            dist[i] = min(dist[i], dist[x] + 1)
            visited[i] = 1
            queue.append(i)

max_dist = 0
count = 0
for idx in range(1, n+1):
    max_dist = max(max_dist, dist[idx])

for i in dist:
    if max_dist == i:
        count += 1

answer = dist.index(max_dist)

print(answer, max_dist, count)
