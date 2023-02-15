import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [0 for _ in range(n+1)]


def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


dfs(v)
print()
visited = [0 for _ in range(n+1)]
bfs(v)
