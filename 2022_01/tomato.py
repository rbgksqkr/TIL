import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomatoes = []
queue = deque()
for i in range(N):
  tomatoes.append(list(map(int, input().split())))
  for j in range(M):
    if tomatoes[i][j] == 1:
      queue.append([i,j])

def bfs():
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= N or dy >= M:
        continue

      if tomatoes[dx][dy] == 0:
        queue.append([dx,dy])
        tomatoes[dx][dy] = tomatoes[x][y] + 1

bfs()
answer = 0
for i in tomatoes:
    for j in i:
        if j == 0:
          print(-1)
          exit(0)
    answer = max(answer, max(i))

print(answer - 1)
