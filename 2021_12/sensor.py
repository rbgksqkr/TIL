import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
betweenNum = []

sensors.sort()

if N < K:
  print(0)
else:
  for i in range(1, N):
    betweenNum.append(sensors[i] - sensors[i-1])
  betweenNum.sort()

  for _ in range(K-1):
    betweenNum.pop()

  print(sum(betweenNum))
