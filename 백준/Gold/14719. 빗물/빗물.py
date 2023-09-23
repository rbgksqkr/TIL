import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]
block = list(map(int, input().split()))


for i in range(m):
  for j in range(0, block[i]):
    graph[j][i] = 1

answer = 0
for i in range(n):
  left, right, rain = 0, 0, 0
  for j in range(m):
    if graph[i][j] == 1:
      if left == 0:
        left = 1
      elif left == 1: # 양쪽이 막혀있으면 고인물
        answer += rain
        rain = 0
    if graph[i][j] == 0 and left == 1:
      rain += 1

print(answer)