import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(input().strip()))


visited = [[0 for _ in range(N)] for _ in range(N)]

def bfs(x, y, flag):
  if visited[x][y] == 1:
    return False
  
  queue = deque([[x, y]])
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]
  color = graph[x][y]

  while queue:
    x, y = queue.popleft()
    visited[x][y] = 1
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]
      
      if dx < 0 or dy < 0 or dx >= N or dy >= N:
        continue    

      if flag == 1 and graph[dx][dy] == 'G':
        graph[dx][dy] = 'R'
          
      if graph[x][y] == graph[dx][dy] == color and visited[dx][dy] == 0:
        queue.append([dx, dy])
        visited[x][y] = 1

  return True


cnt_1, cnt_2 = 0, 0
flag = 0
for i in range(N):
  for j in range(N):
    if bfs(i, j, flag):
      cnt_1 += 1

visited = [[0 for _ in range(N)] for _ in range(N)]
flag = 1
for i in range(N):
  for j in range(N):
    if bfs(i, j, flag):
      cnt_2 += 1

print(cnt_1, cnt_2)
