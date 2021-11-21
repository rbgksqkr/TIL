import sys

input = sys.stdin.readline

N, L = map(int, input().split())
place = list(map(int, input().split()))
count = 0
cur = 0

place.sort()

for i in range(len(place)):
  if cur >= place[i] + 0.5:
    continue
  cur = place[i] - 0.5 + L
  count += 1

print(count)
