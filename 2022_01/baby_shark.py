import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]
x, y = 0, 0
fish = 0
for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    if temp[j] == 9:
      x, y = i, j    
    elif temp[j] != 0:
      fish += 1
  graph.append(temp)

print(graph, fish)

def bfs(x, y):
  queue = deque([[x, y]])
  size = 2
  count = 0
  times = 0
  
  global fish
  if fish == 0:
    print(times)
    return

  mx = [-1, 0, 1, 0]
  my = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= N or dy >= N:
        continue

      elif graph[dx][dy] <= size:
        if graph[dx][dy] == 0 or graph[dx][dy] == size:
          queue.append([dx, dy])
        else:
          count += 1
          fish -= 1
          if size == count:
            size += 1
            count = 0
          queue.append([dx, dy])
        visited[dx][dy] = visited[x][y] + 1
        if fish == 0:
          return

    print(x, y, visited)


bfs(x, y)
print(visited)
