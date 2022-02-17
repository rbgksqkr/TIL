import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
visited = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(M):
  graph.append(list(map(int, input().strip())))

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

def bfs():
  queue = deque([[0, 0]])
  while queue:
    x, y = queue.popleft()

    if x == M-1 and y == N-1:
      return True

    
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= M or dy >= N:
        continue
      
      elif visited[dx][dy] == 0:
        visited[dx][dy] = 1
        if graph[dx][dy] == 1:
          graph[dx][dy] = graph[x][y] + 1
        queue.append([dx, dy])
      
bfs()
print(max(graph[N-1][M-2], graph[N-2][M-2]))
