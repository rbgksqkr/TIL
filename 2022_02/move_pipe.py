import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))
result = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
result[0][0][1] = 1 
# -----------------------------------------------------------
# 첫번째 행 : 가로(0), 세로(1), 대각선(2)으로 갈 수 있는 경우의 수
# 두번째 행, 세번째 행 : 좌표
# result[0][0][1] = 1 : 가로로 (0,1)을 갈 수 있는 경우의 수 : 1
# -----------------------------------------------------------
for i in range(2, N): # 가로로 시작해서 첫번째줄의 가로 dp테이블 초기화
  if graph[0][i] == 0:
    result[0][0][i] = result[0][0][i-1]

for i in range(1, N):
  for j in range(2, N):
    if graph[i][j] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0: # 앞, 아래, 대각선에 길이 있을 때
      #가로+대각선, 세로+대각선, 대각선+대각선
      result[2][i][j] = result[0][i-1][j-1] + result[1][i-1][j-1] + result[2][i-1][j-1]  
    if graph[i][j] == 0:
      result[0][i][j] = result[0][i][j-1] + result[2][i][j-1] # 가로+가로, 대각선+가로
      result[1][i][j] = result[1][i-1][j] + result[2][i-1][j] # 세로+세로, 대각선+세로

print(result[0][N-1][N-1] + result[1][N-1][N-1] + result[2][N-1][N-1]) # 가로, 세로, 대각선 경우의 수의 합
