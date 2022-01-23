import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
graph = []
heights = set({0})
for _ in range(N):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    heights.add(temp[j])
  graph.append(temp)
heights = list(heights)
heights.sort()
idx = 0
cur = heights[idx]
max_height = heights[-1]
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]


def dfs(x, y):
  if x < 0 or y < 0 or x >= N or y >= N:
    return False
  if graph[x][y] > cur and visited[x][y] == 0:
    visited[x][y] = 1
    for i in range(4):
      dfs(x+mx[i], y+my[i])
    return True
    

max_count = 0
while cur < max_height:
  count = 0
  visited = [[0 for _ in range(N)] for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if dfs(i, j):
        count += 1

  if max_count < count:
    max_count = count
  idx += 1
  cur = heights[idx]

print(max_count)
