import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(x, y):
  dx = [-1, 1, 0, 0, -1, -1, 1, 1]
  dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
  if x < 0 or y < 0 or x >= h or y >= w:
    return False
      
  elif graph[x][y] == 1:
    graph[x][y] = 0
    for i in range(8):
      dfs(x+dx[i], y+dy[i])
    return True

  
while True:
  w, h = map(int, input().split())
  graph = []
  visited = [[0 for _ in range(w)] for _ in range(h)]
  count = 0

  if w == 0 and h == 0:
    break

  for _ in range(h):
    graph.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if dfs(i, j):
        count += 1
  
  print(count)
