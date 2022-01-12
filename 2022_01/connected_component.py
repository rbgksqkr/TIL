import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
visited = [0]*(N+1)

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(1, len(graph)+1):
  graph[i].sort()


def dfs(x):
  stack = [x]
  while stack:
    n = stack.pop()
    if visited[n] == 0:
      stack += reversed(graph[n])
      visited[n] = 1
  
  return True


count = 0
for i in range(1, N+1):
  if visited[i] == 0:
    dfs(i)
    count += 1

print(count)
