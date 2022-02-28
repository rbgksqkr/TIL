import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)
plans = []
distance = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
  temp = list(map(int, input().split()))
  for j in range(N):
    if temp[j] == 1:
      distance[i][j+1] = 1
plans += list(map(int, input().split()))

for i in range(1, N+1):
  for j in range(1, N+1):
    if i == j:
      distance[i][j] = 1
      break
      
for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      if distance[i][j] > distance[i][k] + distance[k][j]:
        distance[i][j] = distance[i][k] + distance[k][j]

flag = 0
for i in range(len(plans)-1):
  if distance[plans[i]][plans[i+1]] != INF:
    flag = 1
  else:
    flag = 0
    break

if flag:
  print("YES")
else:
  print("NO")
