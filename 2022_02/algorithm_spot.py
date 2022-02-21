import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[-1 for _ in range(N)] for _ in range(M)]
graph = []
for _ in range(M):
  graph.append(list(map(int, input().strip())))


def bfs(x, y):
  queue = deque()
  queue.append([x, y])
  visited[x][y] = 0
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]

  while queue:
    x, y  = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]
      if dx < 0 or dy < 0 or dx >= M or dy >= N:
        continue
      if visited[dx][dy] == -1:
        if graph[dx][dy] == 0:
          queue.appendleft([dx, dy])
          visited[dx][dy] = visited[x][y]
        elif graph[dx][dy] == 1:
          queue.append([dx, dy])
          visited[dx][dy] = visited[x][y] + 1
  
  print(visited[M-1][N-1])


bfs(0, 0)
