import sys
input = sys.stdin.readline
N = int(input())
d = [0] * (N + 1)
scores = [0]
for _ in range(N):
  scores.append(int(input()))

d[1] = max(scores[0]+scores[1], scores[1])

if N > 1:
  d[2] = max(d[1]+scores[2], scores[0]+scores[2])
  for i in range(3, N+1):
    # 한 계단 vs 두 계단
    d[i] = max(d[i-3]+scores[i-1]+scores[i], d[i-2]+scores[i])

print(d[-1])
