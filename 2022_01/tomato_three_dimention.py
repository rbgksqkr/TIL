import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
graph = []
queue = deque()

for i in range(H):
  temp = []  
  for j in range(N):
    temp.append(list(map(int, input().split())))
  graph.append(temp)

for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1:
        queue.append([i,j,k])

def bfs():
  mx = [0, 0, 0, 0, -1, 1] # 위, 아래, 왼, 오, 앞, 뒤
  my = [0, 0, -1, 1, 0, 0]
  mz = [1, -1, 0, 0, 0, 0]
  while queue:
    z, y, x = queue.popleft()
    for i in range(6):
      dx = x + mx[i]
      dy = y + my[i]
      dz = z + mz[i]
      if dx < 0 or dy < 0 or dz < 0 or dx >= M or dy >= N or dz >= H:
        continue
      elif graph[dz][dy][dx] == 0:
        graph[dz][dy][dx] = graph[z][y][x] + 1
        queue.append([dz, dy, dx])
    
bfs()
answer = 0
for i in graph:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    answer = max(answer, max(j))

print(answer - 1)
