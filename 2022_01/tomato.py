import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomatoes = []
ones = []
for i in range(N):
  temp_list = list(map(int, input().split()))
  if 1 in temp_list:
    y = temp_list.index(1)
    ones.append([i, y]) 
  tomatoes.append(temp_list)

def bfs():
  queue = deque(ones)
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
        days = tomatoes[dx][dy]

  return days

flag = -1

# 저장될 때부터 모든 토마토가 익은 상태
for i in range(N):
  for j in range(M):
    if tomatoes[i][j] == 0:
      flag = 0 # 다 안익음
      break

# 익혀봣는데 토마토가 모두 익지 않은 경우와 다 익은 경우
if flag == -1: # 이미 다 익음
  print(0)
else:
  days = bfs()
  for i in range(N):
    for j in range(M):
      if tomatoes[i][j] == 0: # 못 익음
        flag = 1
        break
  if flag == 1:
    print(-1)
  else:
    print(days-1)
