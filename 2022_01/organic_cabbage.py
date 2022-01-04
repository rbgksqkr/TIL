import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  if x < 0 or y < 0 or x >= N or y >= M:
    return False
  
  if graph[x][y] == 1:
    graph[x][y] = 0
    for i in range(4):
      dfs(x+dx[i], y+dy[i])
    return True

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  graph = [[0 for _ in range(M)] for _ in range(N)]
  count = 0
  
  for i in range(K):
    x, y = map(int, input().split())
    graph[y][x] = 1
  
  for i in range(N):
    for j in range(M):
      if dfs(i, j) == True:
        count += 1
  
  print(count)
