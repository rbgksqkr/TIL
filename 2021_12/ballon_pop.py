import sys
input = sys.stdin.readline
N = int(input())
heights = list(map(int, input().split()))
remainder = [0 for _ in range(1000001)]
count = 0

for i in range(N):
  if remainder[heights[i]] >= 1:
    remainder[heights[i]] -= 1
    remainder[heights[i]-1] += 1
  else:
    count += 1
    remainder[heights[i]-1] += 1

print(count)
