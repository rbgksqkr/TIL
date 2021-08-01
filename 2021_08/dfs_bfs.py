from sys import stdin
from collections import deque

input = stdin.readline

# dfs로 방문
def dfs(graph, v):
  visited = {}
  stack = [v]
  while stack:
    n = stack.pop()
    if n not in visited:
      visited.setdefault(n, 1)
      stack += reversed(graph[n])
  return visited


# bfs로 방문
def bfs(graph, v):
  visited = {}
  queue = deque([v])
  while queue:
    n = queue.popleft()
    if n not in visited: 
      visited.setdefault(n, 1)
      queue += graph[n]

  return visited

# graph 형성
n, m, v = map(int, input().split())
graph = {i:[] for i in range(1,n+1)}

for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y) 
  graph[y].append(x) # 양방향 

for key in graph:
  graph[key].sort() # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문.

print(' '.join(list(map(str,dfs(graph, v)))))
print(' '.join(list(map(str,bfs(graph, v)))))
