import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  graph = {i:[] for i in range(1, N+1)}
  visited = [0 for _ in range(N+1)]
  for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  count = 0
  v = 0
  for i in range(1, N+1):
    if graph[i]:
      v = i
      break
  
  stack = []
  visited[v] = 1
  stack += graph[v]
  while stack:
    n = stack.pop()
    if not visited[n]:
      visited[n] = 1
      count += 1
      stack += graph[n]
  print(count)
