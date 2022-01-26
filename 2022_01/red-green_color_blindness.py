import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
  graph.append(list(input().strip()))


def bfs(x, y):
  queue = deque([[x, y]])
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]
  color = graph[x][y]

  while queue:
    x, y = queue.popleft()
    if visited[x][y] == 0:
      visited[x][y] = 1
      for i in range(4):
        dx = x + mx[i]
        dy = y + my[i]
        
        if dx < 0 or dy < 0 or dx >= N or dy >= N:
          continue    
            
        if graph[dx][dy] == color:
          queue.append([dx, dy])

cnt_1, cnt_2 = 0, 0
flag = 0
for i in range(N):
  for j in range(N):
    if visited[i][j] == 0: 
      bfs(i, j)
      cnt_1 += 1

for i in range(N):
  for j in range(N):
    if graph[i][j] == 'G':
      graph[i][j] = 'R'

visited = [[0 for _ in range(N)] for _ in range(N)]
flag = 1
for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      bfs(i, j)
      cnt_2 += 1

print(cnt_1, cnt_2)
