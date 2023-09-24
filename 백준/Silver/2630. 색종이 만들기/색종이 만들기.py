import sys
from collections import deque
input = sys.stdin.readline

# def dfs(x, y, color):

#   dx = [-1, 1, 0, 0]
#   dy = [0, 0, -1, 1]

#   if x < 0 or y < 0 or x >= n or y >= n:
#     return False
  
#   if graph[x][y] == color:
#     graph[x][y] = -1
#     for i in range(4):
#       dfs(x + dx[i], y + dy[i], color)
#     return True

#   return False

def bfs(graph, color):
  n = len(graph)
  visited = [[0 for _ in range(n)] for _ in range(n)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  queue = deque([[0, 0]])
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      mx = x + dx[i]
      my = y + dy[i]

      if mx < 0 or my < 0 or mx >= n or my >= n:
        continue
      
      if graph[mx][my] != color:
        return False

      if graph[mx][my] == color and not visited[mx][my]:
        visited[mx][my] = 1
        queue.append([mx, my])
  return True



def divideGraph(graph):
  n = len(graph)
  mid = n // 2
  divide = [[], [], [], []]
  
  for i in range(mid):
    temp = []
    for j in range(mid):
      temp.append(graph[i][j])
    divide[0].append(temp)

  for i in range(mid):
    temp = []
    for j in range(mid, n):
      temp.append(graph[i][j])
    divide[1].append(temp)


  for i in range(mid, n):
    temp = []
    for j in range(mid):
      temp.append(graph[i][j])
    divide[2].append(temp)


  for i in range(mid, n):
    temp = []
    for j in range(mid, n):
      temp.append(graph[i][j])
    divide[3].append(temp)
  
  return divide

  

n = int(input())

graphQueue = deque()

tempGraph = []
for _ in range(n):
  tempGraph.append(list(map(int, input().split())))
graphQueue.append(tempGraph)  

white, blue, flag = 0, 0, 0
while graphQueue:
  graph = graphQueue.popleft()
  flag = 1 if graph[0][0] == 1 else 0 # graph가 1로 시작하면 blue에 더하기

  if bfs(graph, flag):
    if flag == 1: blue += 1
    else: white += 1
  else:
    graphArray = divideGraph(graph) # 4등분해서 graphQueue에 넣기
    for i in graphArray: graphQueue.append(i)

print(white)
print(blue)