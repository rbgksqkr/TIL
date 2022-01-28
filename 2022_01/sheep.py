import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
wolfs = []
sheeps = []
visited = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
  temp = list(input().strip())
  for j in range(len(temp)):
    if temp[j] == 'v':
      wolfs.append([i,j])
    if temp[j] == 'o':
      sheeps.append([i,j])
  graph.append(temp)
total_wolf = len(wolfs)
total_sheep = len(sheeps)


def bfs(x, y):
  queue = deque([[x,y]])
  global total_wolf, total_sheep
  wolf = 0
  sheep = 0
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]
      if dx < 0 or dy < 0 or dx >= R or dy >= C or graph[dx][dy] == '#':
        continue
      if visited[dx][dy] == 0:
        visited[dx][dy] = 1
        if graph[dx][dy] == 'v':
          wolf += 1
        elif graph[dx][dy] == 'o':
          sheep += 1
        queue.append([dx,dy])

  if sheep:
    if wolf >= sheep:
      total_sheep -= sheep
    else:
      total_wolf -= wolf


for wolf in wolfs:
  bfs(wolf[0], wolf[1])
print(total_sheep, total_wolf)
