import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
  queue = deque([[x, y]])
  flag = 1
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]
      if dx < 0 or dy < 0 or dx >= N or dy >= M:
        continue
      if graph[dx][dy] == 0:
        graph[dx][dy] = graph[x][y] + 1
        queue.append([dx, dy])
    
    if not queue and flag == 1: # 벽 한번 뚫기
      for i in range(4):
        dx = x + mx[i]
        dy = y + my[i]
        if dx < 0 or dy < 0 or dx >= N or dy >= M:
          continue
        graph[dx][dy] = graph[x][y] + 1
        queue.append([dx, dy])
      flag = 0
    
    print(graph, queue)

N, M = map(int, input().split())
graph = []

for _ in range(N):
  graph.append(list(map(int, input().strip())))

bfs(0, 0)

if graph[N-1][M-1]:
  print(graph[N-1][M-1]+1)
else:
  print(-1)
