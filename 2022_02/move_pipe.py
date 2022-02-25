import sys
input = sys.stdin.readline

N = int(input())
graph = []
dp = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(N):
  graph.append(list(map(int, input().split())))

degree = 0 # 가로 : 0, 세로 : 1, 대각선 : 2
answer = 0
def dfs(x, y, degree):
  global answer
  if x == N-1 and y == N-1: # 목적지에 도착하면 +1
    answer += 1
    return

  if degree == 0 or degree == 2: # 앞으로 전진하는 경우
    if y+1 < N:
      if graph[x][y+1] == 0:
        dfs(x, y+1, 0) # 전진하면 모양은 가로가 되므로 degree = 0
  if degree == 1 or degree == 2:  # 아래로 내려가는 경우
    if x+1 < N:
      if graph[x+1][y] == 0:
        dfs(x+1, y, 1) # 내려가면 모양은 세로가 되므로 degree = 1
  if degree == 0 or degree == 1 or degree == 2: # 대각선으로 내려가는 경우
    if x+1 < N and y+1 < N:
      if graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
        dfs(x+1, y+1, 2) # 대각선 모양 유지 degree = 2

dfs(0, 1, 0)
print(answer)
