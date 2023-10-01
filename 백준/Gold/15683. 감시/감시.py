import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

mode = [
  [], 
[[0], [1], [2], [3]],
[[0, 2], [1, 3]],
[[0, 1], [1, 2], [2, 3], [3, 0]],
[[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
[[0, 1, 2, 3]]
]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
cameras = []
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(m):
    if 1 <= line[j] <= 5:
      cameras.append([line[j], i, j])
  graph.append(line)
  


def printGraph(graph):
  for i in range(len(graph)):
    for j in range(len(graph[0])):
      print(graph[i][j], end=' ')
    print()
  print()


def getResult(graph):
  count = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        count += 1
  return count
  

def fill(graph, dir, x, y):
  for i in dir:
    mx, my = x, y
    while True:
      mx += dx[i]
      my += dy[i]
      if mx < 0 or my < 0 or mx >= n or my >= m:
        break

      if graph[mx][my] == 6:
        break

      if graph[mx][my] == 0:
        graph[mx][my] = '#'


def dfs(index, graph):
  global answer
  if index == len(cameras):
    count = getResult(graph)
    answer = min(answer, count)
    return

  copy_graph = copy.deepcopy(graph)
  num, x, y = cameras[index]
  for i in mode[num]:
    fill(copy_graph, i, x, y)
    dfs(index+1, copy_graph)
    copy_graph = copy.deepcopy(graph)
  
  
answer = int(1e9)
dfs(0, graph)
print(answer)
