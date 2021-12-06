import sys
input = sys.stdin.readline

T = int(input())
times = [300, 60, 10]
counts = [0, 0, 0]

for i in range(3):
  counts[i] += T // times[i]
  T %= times[i]

if T == 0:
  [print(i, end=" ") for i in counts]
else:
  print(-1)
