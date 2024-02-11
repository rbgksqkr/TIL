import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs():
    visited = [0 for _ in range(n+1)]
    queue = deque([v])
    visited[v] = 1
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for j in graph[cur]:
            if visited[j]:
                continue
            queue.append(j)
            visited[j] = 1

def dfs():
    visited = [0 for _ in range(n+1)]
    stack = []
    stack.append(v)
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        visited[cur] = 1
        print(cur, end=' ')
        for j in range(len(graph[cur])-1, -1, -1):
            if visited[graph[cur][j]]:
                continue
            stack.append(graph[cur][j])

dfs()
print()
bfs()