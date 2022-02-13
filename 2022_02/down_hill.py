import sys
input = sys.stdin.readline

M, N = map(int, input().split())

graph = []

for _ in range(M):
  graph.append(list(map(int, input().split())))

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]


def dfs():
  stack = [[0, 0]]
  count = 0
  while stack:
    x, y = stack.pop()
    if graph[x][y] == graph[M-1][N-1]:
      count += 1
      continue
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= M or dy >= N:
        continue
  
      if graph[x][y] > graph[dx][dy]:
        stack.append([dx, dy])

  return count


print(dfs())
