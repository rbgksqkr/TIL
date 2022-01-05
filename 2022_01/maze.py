import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
mazes = []
for _ in range(N):
  mazes.append(list(map(int, input().strip())))

def bfs(x, y):
  queue = deque()
  queue.append([x,y])
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]
      if dx < 0 or dy < 0 or dx >= N or dy >= M:
        continue
      elif mazes[dx][dy] == 1:
        mazes[dx][dy] = mazes[x][y] + 1
        queue.append([dx, dy])

  return mazes[-1][-1]

print(bfs(0, 0))
