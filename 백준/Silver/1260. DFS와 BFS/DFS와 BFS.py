from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()


def dfs(x):
    visited[x] = 1
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


visited = [0 for _ in range(n+1)]
dfs(v)
print()
visited = [0 for _ in range(n+1)]
bfs(v)
