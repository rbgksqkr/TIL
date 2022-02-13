import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)] # 내리막길 경우의 수

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]


def dfs(x, y):
  if x == m-1 and y == n-1: # 목적지까지 가면 경로가 있으니까 +1
      return 1

  if dp[x][y] == -1: # 안가봤으면
      dp[x][y] = 0 # 목적지까지 못간다고 가정하고
      for i in range(4):
        dx = x + mx[i]
        dy = y + my[i]
        if 0 <= dx < m and 0 <= dy < n:
            if graph[dx][dy] < graph[x][y]: # 내리막길이면
                dp[x][y] += dfs(dx, dy) # 재귀

  return dp[x][y] # 이전의 연산한 방문경로가 있으므로 그 값 반환


print(dfs(0, 0))
