import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
gap = []

sensors.sort()

if N < K:
  print(0)
else:
  for i in range(1, N):
    gap.append(sensors[i] - sensors[i-1])
  gap.sort()

  for _ in range(K-1):
    gap.pop()

  print(sum(gap))
