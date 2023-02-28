import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
e = int(input())
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]


def dfs(x):
    if x == y:
        return
    for i in graph[x]:
        if not visited[i]:
            visited[i] = visited[x] + 1
            dfs(i)


dfs(x)
if visited[y]:
    print(visited[y])
else:
    print(-1)
