import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
canvas = []
for _ in range(n):
  canvas.append(list(map(int, input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  queue = deque([[x,y]])
  visited[x][y] = 1
  count = 1
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= n or dy >= m:
        continue
      
      elif canvas[dx][dy] == 1 and visited[dx][dy] == 0:
        visited[dx][dy] = 1
        count += 1
        queue.append([dx,dy])
  
  return count
        

total = 0
max_count = 0
for i in range(n):
  for j in range(m):
    if visited[i][j] == 0 and canvas[i][j] == 1:
        max_count = max(bfs(i, j), max_count)
        count = 0
        total += 1

print(total)
if total:
  print(max_count)
else:
  print(0)