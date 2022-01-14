import sys
input = sys.stdin.readline

N = int(input())

graph = {i:[] for i in range(N)}
visited = [0 for _ in range(N)]
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    if temp[j] == 1:
      graph[i].append(j)


def dfs(n):
  stack = [n]

  while stack:
    n = stack.pop()

    if not visited[n]:

      for i in graph[n]:
        arr[n][i] = 1
        arr[i][n] = 1
      visited[n] = 1
      stack += graph[n]


for i in range(N):
  if graph[i]:
    dfs(i)
print(arr)
