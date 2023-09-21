import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

while True:
  m, n = map(int, input().split())

  if m == 0 or n == 0:
    break

  data = []
  for _ in range(n):
    data.append(list(map(int, input().split())))

  dx = [-1, -1, 0, 1, 1, 1, 0, -1]
  dy = [0, 1, 1, 1, 0, -1, -1, -1]

  def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
      return False
    
    if data[x][y] == 1:
      data[x][y] = 0
      for i in range(8):
        dfs(x+dx[i], y+dy[i])
      return True
    return False

  answer = 0
  for i in range(n):
    for j in range(m):
      if dfs(i, j):
        answer += 1
  print(answer)