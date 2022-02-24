import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
dp = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
  graph.append(list(map(int, input().split())))

print(graph)
print(dp)

def bfs(x, y):
  queue = deque()
  queue.append([x, y, 0])
  dp[x][y] = 1

  # # 가로, 대각선 아래, 대각선 위, 세로
  # mx = [0, 1, -1, 1]
  # my = [1, 1, -1, 0]
  degree = 0 # 가로 : 0, 세로 : 1, 대각선 : 2
  while queue:
    x, y = queue.popleft()
    # dp 테이블에 있으면 그 값 쓰고 없으면 탐색
    if degree == 0: # 가로
      if graph[x][y+1] == 0:
        dp[x][y+1] = dp[x][y] + 1
        queue.append([x, y+1, 0])

      if graph[x+1][y+1] == 0:
        dp[x+1][y+1] = dp[x][y] + 1
        queue.append([x+1, y+1, 1])
        

    if degree == 1: # 세로
      if graph[x][y+1] == 0:
        dp[x][y+1] = dp[x][y] + 1

      if graph[x+1][y+1] == 0:
        dp[x+1][y+1] = dp[x][y] + 1

    if degree == 2: # 대각선
      if graph[x][y+1] == 0:
        dp[x][y+1] = dp[x][y] + 1

      if graph[x+1][y+1] == 0:
        dp[x+1][y+1] = dp[x][y] + 1        
    
