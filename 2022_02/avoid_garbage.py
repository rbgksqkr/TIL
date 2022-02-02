import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
trash = []
for i in range(K):
  r, c = map(int, input().split())
  graph[r-1][c-1] = 1
  trash.append([r, c])


def bfs(x, y):
  queue = deque([[x, y]])
  visited[x][y] = 1
  count = 1
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= N or dy >= M:
        continue

      if graph[dx][dy] == 1 and visited[dx][dy] == 0:
        visited[dx][dy] = 1
        count += 1
        queue.append([dx, dy])
    
  return count


max_count = 0
while trash:
  i, j = trash.pop()
  i, j = i-1, j-1
  if graph[i][j] == 1 and visited[i][j] == 0:
    max_count = max(max_count, bfs(i, j))
print(max_count)
