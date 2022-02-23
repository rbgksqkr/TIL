import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().strip())))

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]


def bfs(x, y):
  queue = deque()
  queue.append([x, y])
  distance = [[-1 for _ in range(n)] for _ in range(n)]
  distance[x][y] = 0
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= n or dy >= n:
        continue

      if distance[dx][dy] == -1:
        if graph[dx][dy] == 1:
          distance[dx][dy] = distance[x][y]
          queue.appendleft([dx, dy])
        elif graph[dx][dy] == 0:
          distance[dx][dy] = distance[x][y] + 1
          queue.append([dx, dy])
  
  print(distance[n-1][n-1])

       
bfs(0, 0)
