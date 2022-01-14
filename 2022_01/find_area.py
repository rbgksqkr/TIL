import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
  lbottom_x, lbottom_y, rtop_x, rtop_y = map(int, input().split())
  for i in range(M - rtop_y, M - lbottom_y):
    for j in range(lbottom_x, rtop_x):
      graph[i][j] = 1


def dfs(x, y):
  global count

  dx = [-1, 1, 0 ,0]
  dy = [0, 0, -1, 1]

  if x < 0 or y < 0 or x >= M or y >= N:
    return False
  
  elif graph[x][y] == 0:
    graph[x][y] = 1
    count += 1
    for i in range(4):
      dfs(x+dx[i], y+dy[i])
    return True

answer = []
count = 0
for i in range(M):
  for j in range(N):
    if dfs(i, j):
      answer.append(count)
      count = 0


answer.sort()
print(len(answer))
for i in answer:
  print(i, end=' ')
