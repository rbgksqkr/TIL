import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]
x, y = 0, 0
fish = 0
size = 2
count = 0
for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    if temp[j] == 9:
      x, y = i, j    
    elif temp[j] != 0:
      fish += 1
  graph.append(temp)


def dfs(x, y, size):
  global count
  global fish
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  if x < 0 or y < 0 or x >= N or y >= N:
    return False
  
  if graph[x][y] <= size:
    if graph[x][y] != 0 and graph[x][y] != size:
      count += 1
      fish -= 1
      if size == count:
        size += 1
        count = 0

    for i in range(4):
      dfs(x+dx[i], y+dy[i], size)
    return True


dfs(x, y, size)
