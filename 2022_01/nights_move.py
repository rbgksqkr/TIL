import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
  mx = [2, 1, -1, -2, -2, -1, 1, 2]
  my = [1, 2, 2, 1, -1, -2, -2, -1]

  while queue:
    x, y = queue.popleft()
    for i in range(8):
      dx = x + mx[i]
      dy = y + my[i]
      if dx < 0 or dy < 0 or dx >= I or dy >= I:
        continue
      if graph[dx][dy] == 0:
        graph[dx][dy] = graph[x][y] + 1
        queue.append([dx, dy])

T = int(input())

for _ in range(T):
  I = int(input())
  x, y = map(int, input().split())
  queue = deque([])
  queue.append([x,y])
  lx, ly = map(int, input().split())
  graph = [[0] * I for _ in range(I)]
  if x == lx and y == ly:
    print(0)
  else:
    bfs(x,y)
    print(graph[lx][ly])
