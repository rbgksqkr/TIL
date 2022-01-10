import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  queue = deque([[0, 0, 1]])
  visited = [[[0]*2 for i in range(M)] for j in range(N)]
  visited[0][0][1] = 1
  while queue:
    x, y, w = queue.popleft() # w == 1 일 때 벽을 뚫을 수 있음

    if x == N-1 and y == M-1:
      return visited[x][y][w]

    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]

    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= N or dy >= M:
        continue
      
      if graph[dx][dy] == 1 and w == 1: # 벽이 있고 뚫을 수 있는 경우
        visited[dx][dy][0] = visited[x][y][1] + 1
        queue.append([dx, dy, 0])
      
      elif graph[dx][dy] == 0 and visited[dx][dy][w] == 0: # 벽이 없고 안가본 경우(일반적인 진행)
        visited[dx][dy][w] = visited[x][y][w] + 1
        queue.append([dx, dy, w])
  
  return -1

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().strip())))

print(bfs())
