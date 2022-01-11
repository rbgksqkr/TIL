import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

graph = [0 for _ in range(100001)]


def bfs(x):
  queue = deque([x])
  while queue:
    x = queue.popleft()
    if x == K:
      print(graph[x])
      break

    d = [x-1, x+1, 2*x]

    for i in range(3):
      dx = d[i]
      if 0 <= dx <= 100000 and graph[dx] == 0:
        graph[dx] = graph[x] + 1
        queue.append(dx)

bfs(N)
