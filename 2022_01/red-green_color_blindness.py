import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(input().strip()))

visited = [[0 for _ in range(N)] for _ in range(N)]

def dfs(x, y, flag):

  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]

  if x < 0 or y < 0 or x >= N or y >= N:
    return False

  if graph[x][y] == 'R' and flag == 1:
    visited[x][y] = 1
    graph[x][y] = 0
    for i in range(4):
      dfs(x + mx[i], y + my[i], flag)
    return True

  if graph[x][y] == 'G' and flag == 2:
    visited[x][y] = 1
    graph[x][y] = 0
    for i in range(4):
      dfs(x + mx[i], y + my[i], flag)
    return True

  if graph[x][y] == 'B' and flag == 3:
    visited[x][y] = 1
    graph[x][y] = 0
    for i in range(4):
      dfs(x + mx[i], y + my[i], flag)
    return True

count = 0  
flag = 1
for k in range(3):
  for i in range(N):
    for j in range(N):
      if dfs(i, j, flag):
        count += 1
  flag += 1

print(count)
