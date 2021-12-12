import sys
input = sys.stdin.readline
N, K = map(int, input().split())
heights = list(map(int, input().split()))
diff = []

for i in range(1, N):
  diff.append(heights[i] - heights[i-1])

diff.sort()
for _ in range(K-1):
  diff.pop()

print(sum(diff))
