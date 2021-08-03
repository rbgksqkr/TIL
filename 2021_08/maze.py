from sys import stdin
input = stdin.readline
N, M = list(map(int, input().split()))

answer = 1

# 길 탐색
def dfs(maze):
  visited = []
  stack = []
  Pos = [1, 1]
  while True:
    n = stack.pop()
    Pos = n

    if Pos[1] - M == 1: # 위
      stack.append(Pos)
    if Pos[1] + 1 == 1: # 오른쪽
      stack.append(Pos)
    if Pos[1] + M == 1: # 아래
      stack.append(Pos)
    if Pos[1] - 1 == 1: # 왼쪽
      stack.append(Pos)




# 미로 만들기
maze = []

for i in range(N):
  maze.append(list(map(str, stdin.readline().split())))


dfs(maze)
