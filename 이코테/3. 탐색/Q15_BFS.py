import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
INF = int(1e9)
distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance[x] = 0
queue = deque([x])
while queue:
    now = queue.popleft()

    for i in graph[now]:
        if distance[i] == INF:
            distance[i] = distance[now] + 1
            queue.append(i)

flag = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = 1

if flag == 0:
    print(-1)