import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

vacc_up, vacc_down = [], []
graph = []
mise = []
for i in range(R):
  row = list(map(int, input().split()))
  for j in range(C):
    if row[j] > 0:
      mise.append([i, j, 0])
  graph.append(row)

# 진공 청소기 위치 저장
for i in range(R):
  if graph[i][0] == -1:
    if graph[i][0]:
      vacc_up = [i, 0]
      vacc_down = [i+1, 0]
      break


dx = [-1, 0, 1, 0] # 위부터 시계방향
dy = [0, 1, 0, -1]


def spread():
  mise_graph = [[0 for _ in range(C)] for _ in range(R)]

  for x in range(R):
    for y in range(C):
      if graph[x][y] == 0 or graph[x][y] == -1:
        continue
    
      for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or my < 0 or mx >= R or my >= C:
          continue

        if graph[mx][my] == -1:
          continue

        mise_graph[mx][my] += graph[x][y] // 5
        mise_graph[x][y] -= graph[x][y] // 5
  for i in range(R):
    for j in range(C):
      graph[i][j] += mise_graph[i][j]


def getSum(graph):
  mise_sum = 0
  row = len(graph)
  col = len(graph[0])
  for i in range(row):
    for j in range(col):
      if graph[i][j] != -1:
        mise_sum += graph[i][j]
  return mise_sum


def clean_top():
    dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)
    x, y, d = vacc_up[0], 1, 0
    prev = 0

    while True:
        mx, my = x + dx[d], y + dy[d]

        if x == vacc_up[0] and y == 0:
            break
        if not 0 <= mx < R or not 0 <= my < C:
            d += 1
            continue

        graph[x][y], prev = prev, graph[x][y]
        x, y = mx, my


def clean_bottom():
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    x, y, d = vacc_down[0], 1, 0
    prev = 0

    while True:
        mx, my = x + dx[d], y + dy[d]

        if x == vacc_down[0] and y == 0:
            break
        if not 0 <= mx < R or not 0 <= my < C:
            d += 1
            continue

        graph[x][y], prev = prev, graph[x][y]
        x, y = mx, my

for _ in range(T):
  spread()
  clean_top()
  clean_bottom()

print(getSum(graph))