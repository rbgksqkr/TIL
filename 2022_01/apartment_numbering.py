import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().strip())))




visited = [[0]*N]*N
print(graph)
print(visited)
def dfs(x, y):
  count = 0
  x, y = 0, 0
  moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
  dx, dy = x, y
  while True:
    for i in range(4):
      dx = x + moves[i][0]
      dy = y + moves[i][1]

      if dx < 0 or dy < 0 or dx >= N or dy >= N: # 길 아님
        continue
      
      if graph[dy][dx] == 1 and visited[dy][dx] == 0: # 집인데 안가봄
        visited[dy][dx] = 1
        count += 1
        x, y = dx, dy
        break

      elif graph[dy][dx] == 0 and visited[dy][dx] == 0: # 집 없는데 안가봄
        graph[dy][dx] = 1
        visited[dy][dx] = 1
        x, y = dx, dy
        break
      
      print(dx, dy)
    if visited[x][y] == 0:
      break


  return count

answer = []
for i in range(N):
  for j in range(N):
      answer.append(dfs(i,j))
