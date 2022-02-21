import sys
input = sys.stdin.readline

N = int(input())
INF = int(1e9)
distance = [[INF for _ in range(N)] for _ in range(N)] # 거리 무한으로 초기화
for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    if temp[j] == 1:
      distance[i][j] = 1 # 이어지는 정점 간의 거리 존재 유무

for k in range(N):
  for i in range(N):
    for j in range(N):
      if distance[i][j] > distance[i][k] + distance[k][j]: # 어떻게든 가는 길이 있으면
        distance[i][j] = distance[i][k] + distance[k][j] # 무한보다 작기 때문에 값 바뀜.

for i in range(N):
  for j in range(N):
    if distance[i][j] == INF:
      print(0, end=' ')
    else:
      print(1, end=' ')
  print()
